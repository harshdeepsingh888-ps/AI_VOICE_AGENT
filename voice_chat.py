from app.services.speech_service import listen
from app.services.llm_service import llm_service
from app.tools import app_launcher, calculator_tool
from app.tools.tool_dispatcher import tool_dispatcher

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

        tool_response = tool_dispatcher.execute(user_text)

        if tool_response:
            print(f"\nTool: {tool_response}\n")
            continue

        ai_response = llm_service.generate_response(
            session_id=session_id,
            message=user_text,
        )

        print(f"\nAI: {ai_response}\n")

    except KeyboardInterrupt:
        print("\n\nAI Voice Agent stopped.")
        break

    except Exception as e:
        print(f"\nError: {e}")
        print("Continuing...\n")