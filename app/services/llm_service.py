from google import genai
import asyncio

from app.core.config import settings
from app.services.memory_service import memory_service
from app.services.tts_service import tts_service

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMService:

    def generate_response(self, session_id: str, message: str):
        memory_service.add_message(session_id, "user", message)

        history = memory_service.get_history(session_id)

        prompt = ""

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