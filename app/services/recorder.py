import sounddevice as sd
import numpy as np
import webrtcvad
import wave


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
        self.max_silence_frames = 30

        print("✅ Recorder initialized")

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        # Convert microphone data to 16-bit PCM
        pcm = (indata * 32767).astype(np.int16).tobytes()

        # Speech detected
        if self.vad.is_speech(pcm, self.sample_rate):

            if not self.recording:
                print("🟢 Speech detected!")
                print("🎙️ Recording...")

                self.recording = True

            self.frames.append(pcm)

            # Reset silence counter
            self.silence_frames = 0

        # Silence detected
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
            wf.setsampwidth(2)  # int16 = 2 bytes
            wf.setframerate(self.sample_rate)
            wf.writeframes(b"".join(self.frames))

        print(f"✅ Audio saved as {filename}")