from app.services.recorder import Recorder

recorder = Recorder()

recorder.wait_for_speech()

print("✅ Done!")