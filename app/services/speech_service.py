import whisper
import sounddevice as sd
from scipy.io.wavfile import write

# Load the Whisper model only once
model = whisper.load_model("base")


def record_audio(filename="recording.wav", duration=5, sample_rate=16000):
    print("🎤 Recording...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, sample_rate, audio)

    print(f"✅ Audio saved as {filename}")


def transcribe_audio(filename="recording.wav"):
    print("📝 Transcribing...")

    result = model.transcribe(filename)

    print(f"🗣️ You said: {result['text']}")

    return result["text"]


def listen():
    record_audio()
    text = transcribe_audio()
    return text