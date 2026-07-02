import whisper


class SpeechService:
    def __init__(self):
        print("🎤 Loading Whisper model...")
        self.model = whisper.load_model("base")
        print("✅ Whisper model loaded!")

    def transcribe_audio(self, audio_path: str):
        result = self.model.transcribe(audio_path)
        return result["text"]


speech_service = SpeechService()