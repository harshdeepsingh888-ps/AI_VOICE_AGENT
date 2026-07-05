import sounddevice as sd
import numpy as np


class VADService:
    def __init__(self):
        self.threshold = 500

    def get_volume(self, indata):
        return np.max(np.abs(indata))


vad_service = VADService()