from google import genai
import asyncio
import json

from app.core.config import settings
from app.schemas.tool_plan import ToolPlan
from app.services.memory_service import memory_service
from app.services.tts_service import tts_service
from app.tools.tool_manager import tool_manager

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMService:

    def _build_tools_context(self) -> str:
        tools = tool_manager.registry.get_tool_metadata()

        if not tools:
            return "No tools are currently available."

        context = "Available tools:\n"

        for tool in tools:
            context += (
                f"- Name: {tool['name']}\n"
                f"  Description: {tool['description']}\n"
                f"  Version: {tool['version']}\n"
                f"  Enabled: {tool['enabled']}\n"
            )

        return context

    def plan_tool_usage(self, message: str) -> ToolPlan:
        prompt = f"""
You are a tool planning system.

Your job is to decide whether the user's message needs a tool.

{self._build_tools_context()}

Return only valid JSON.

Rules:
- If a tool is needed, return:
{{
  "use_tool": true,
  "tool_name": "tool_name_here",
  "arguments": {{
    "user_message": "original user message here"
  }}
}}

- If no tool is needed, return:
{{
  "use_tool": false,
  "tool_name": null,
  "arguments": {{}}
}}

User message:
{message}
"""

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            print("RAW PLANNER RESPONSE:", response.text)

            raw_text = response.text.strip()

            if raw_text.startswith("```json"):
                 raw_text = raw_text.replace("```json", "").replace("```", "").strip()
            elif raw_text.startswith("```"):
                 raw_text = raw_text.replace("```", "").strip()

            data = json.loads(raw_text)

            return ToolPlan(
                use_tool=data.get("use_tool", False),
                tool_name=data.get("tool_name"),
                arguments=data.get("arguments", {}),
            )

        except Exception as e:
            return ToolPlan(
                use_tool=False,
                tool_name=None,
                arguments={},
                error=str(e),
            )

    def generate_response(self, session_id: str, message: str):
        memory_service.add_message(session_id, "user", message)

        history = memory_service.get_history(session_id)

        prompt = self._build_tools_context()
        prompt += "\n\nConversation:\n"

        for chat in history:
            if chat["role"] == "user":
                prompt += f"User: {chat['content']}\n"
            else:
                prompt += f"Assistant: {chat['content']}\n"

        prompt += "Assistant:"

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            ai_text = response.text

            memory_service.add_message(session_id, "assistant", ai_text)

            asyncio.run(tts_service.text_to_speech(ai_text))

            return ai_text

        except Exception as e:
            error_text = str(e)

            if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                return "Gemini quota is currently exhausted. Please try again later."

            if "503" in error_text or "UNAVAILABLE" in error_text:
                return "Gemini is temporarily unavailable. Please try again later."

            return "Sorry, something went wrong while generating a response."


llm_service = LLMService()