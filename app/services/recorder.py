import sounddevice as sd
import numpy as np
import webrtcvad
import wave
from collections import deque


class Recorder:

    def __init__(self):
        self.sample_rate = 16000
        self.channels = 1
        self.frame_duration = 30
        self.frame_size = int(
            self.sample_rate * self.frame_duration / 1000
        )

        self.vad = webrtcvad.Vad(2)

        self.frames = []
        self.recording = False

        self.silence_frames = 0
        self.max_silence_frames = 45

        # Stores audio just before speech starts
        self.pre_buffer_frames = 15
        self.pre_buffer = deque(maxlen=self.pre_buffer_frames)

        print("✅ Recorder initialized")

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        pcm = (indata * 32767).astype(np.int16).tobytes()

        is_speech = self.vad.is_speech(pcm, self.sample_rate)

        if not self.recording:
            self.pre_buffer.append(pcm)

        if is_speech:

            if not self.recording:
                print("🟢 Speech detected!")
                print("🎙️ Recording...")

                self.recording = True

                # Add audio from just before speech started
                self.frames.extend(list(self.pre_buffer))

            self.frames.append(pcm)
            self.silence_frames = 0

        else:

            if self.recording:
                self.frames.append(pcm)
                self.silence_frames += 1

                if self.silence_frames >= self.max_silence_frames:
                    print("🔇 Silence detected.")
                    self.recording = False

    def wait_for_speech(self, filename="recording.wav"):

        print("🎤 Waiting for speech...")

        self.frames = []
        self.recording = False
        self.silence_frames = 0
        self.pre_buffer.clear()

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            blocksize=self.frame_size,
            dtype="float32",
            callback=self.callback,
        ):

            while True:
                sd.sleep(100)

                if not self.recording and len(self.frames) > 0:
                    break

        print("💾 Saving recording...")

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(b"".join(self.frames))

        print(f"✅ Audio saved as {filename}")