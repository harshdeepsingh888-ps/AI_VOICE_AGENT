from app.services.speech_service import listen

input("Press Enter to start recording...")

text = listen()

print(f"\nFinal Text: {text}")