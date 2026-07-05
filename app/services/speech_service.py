import whisper
import sounddevice as sd
import numpy as np
import webrtcvad

# Load Whisper only once
model = whisper.load_model("base")


def record_audio_vad(filename="recording.wav"):
    print("🎤 Waiting for speech...")

    vad = webrtcvad.Vad(2)

    sample_rate = 16000
    frame_duration = 30  # milliseconds
    frame_size = int(sample_rate * frame_duration / 1000)

    speech_detected = False

    def callback(indata, frames, time, status):
        nonlocal speech_detected

        if status:
            print(status)

        pcm = (indata * 32767).astype(np.int16).tobytes()

        if vad.is_speech(pcm, sample_rate):
            if not speech_detected:
                speech_detected = True
                print("🟢 Speech detected!")

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        blocksize=frame_size,
        dtype="float32",
        callback=callback,
    ):
        while not speech_detected:
            sd.sleep(100)

    print("===================================")
    print("🎉 FUNCTION COMPLETED SUCCESSFULLY")
    print("===================================")


def transcribe_audio(filename="recording.wav"):
    print("📝 Transcribing...")

    result = model.transcribe(filename)

    print(f"🗣️ You said: {result['text']}")

    return result["text"]


def listen():
    record_audio_vad()
    text = transcribe_audio()
    return text