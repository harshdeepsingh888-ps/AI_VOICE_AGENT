import sounddevice as sd
import webrtcvad

vad = webrtcvad.Vad(2)  # Aggressiveness: 0-3

sample_rate = 16000
frame_duration = 30  # milliseconds

frame_size = int(sample_rate * frame_duration / 1000)

print("🎤 Listening...")
print("Speak into the microphone (Ctrl+C to stop)\n")


def callback(indata, frames, time, status):
    if status:
        print(status)

    pcm = (indata * 32767).astype("int16").tobytes()

    is_speech = vad.is_speech(pcm, sample_rate)

    if is_speech:
        print("🟢 Speech")
    else:
        print("⚫ Silence")


with sd.InputStream(
    samplerate=sample_rate,
    channels=1,
    blocksize=frame_size,
    dtype="float32",
    callback=callback,
):
    while True:
        sd.sleep(100)