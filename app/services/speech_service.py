
import whisper

from app.services.recorder import Recorder

# Load Whisper only once
model = whisper.load_model("base")

recorder = Recorder()


def transcribe_audio(filename="recording.wav"):
    print("📝 Transcribing...")

    result = model.transcribe(filename, language="en")

    print(f"🗣️ You said: {result['text']}")

    return result["text"]


def listen():
    recorder.wait_for_speech()
    text = transcribe_audio()
    return text