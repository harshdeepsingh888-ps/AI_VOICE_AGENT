from app.services.speech_service import listen
from app.services.speech_normalizer import speech_normalizer
from app.services.agent_service import agent_service
from app.tools import (
    app_launcher,
    calculator_tool,
    weather_tool,
)

print("=" * 50)
print("AI Voice Agent Started")
print("Say 'exit' to quit.")
print("=" * 50)

session_id = "voice_session"

while True:
    try:
        user_text = listen()

        print(f"\nYou: {user_text}")

        clean_text = user_text.lower().strip()

        if not clean_text:
            print("\nNo speech detected. Listening again...")
            continue

        if "exit" in clean_text or "quit" in clean_text or "stop" in clean_text:
            print("\nGoodbye!")
            break

        print("\nThinking...")

        normalized_text = speech_normalizer.normalize(user_text)
        print(f"Normalized: {normalized_text}")

        response = agent_service.process(
            session_id=session_id,
            message=normalized_text,
        )

        print(f"\nAI: {response}\n")

    except KeyboardInterrupt:
        print("\n\nAI Voice Agent stopped.")
        break

    except Exception as e:
        print(f"\nError: {e}")
        print("Continuing...\n")