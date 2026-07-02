from app.services.speech_service import speech_service

print("🎤 Starting Speech-to-Text Test...")

text = speech_service.transcribe_audio("Recording.m4a")

print("\n✅ Recognized Text:")
print(text)