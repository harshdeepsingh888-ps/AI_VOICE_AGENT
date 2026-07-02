import asyncio
from app.services.tts_service import tts_service

print("🔊 Testing Text-to-Speech...")

async def main():
    await tts_service.text_to_speech(
        "Hello Harshdeep. I am your AI Voice Agent."
    )

asyncio.run(main())