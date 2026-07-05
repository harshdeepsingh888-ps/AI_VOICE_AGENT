import sounddevice as sd
import numpy as np

print("Default devices:", sd.default.device)
print()

def callback(indata, frames, time, status):
    print("Max:", np.max(np.abs(indata)))

print("🎤 Speak loudly into your microphone...")
print("Press Ctrl+C to stop.\n")

with sd.InputStream(
    samplerate=16000,
    channels=1,
    dtype="int16",
    callback=callback,
):
    while True:
        sd.sleep(100)