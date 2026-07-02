from google import genai
from app.core.config import settings
from app.services.memory_service import memory_service
from app.services.tts_service import tts_service

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMService:

    def generate_response(self, session_id: str, message: str):

        # Store user message
        memory_service.add_message(session_id, "user", message)

        # Get conversation history
        history = memory_service.get_history(session_id)

        # Convert history into a prompt
        prompt = ""

        for chat in history:
            if chat["role"] == "user":
                prompt += f"User: {chat['content']}\n"
            else:
                prompt += f"Assistant: {chat['content']}\n"

        prompt += "Assistant:"

        # Call Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text

        # Save AI response
        memory_service.add_message(session_id, "assistant", ai_text)

        import asyncio

        asyncio.run(tts_service.text_to_speech(ai_text))

        return ai_text


llm_service = LLMService()