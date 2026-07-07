class SpeechNormalizer:
    """
    Cleans common Whisper transcription mistakes before
    sending the text to the Tool Dispatcher or Gemini.
    """

    def __init__(self):
        self.replacements = {
            "warp is": "what is",
            "water is": "what is",
            "what's": "what is",
            "note pad": "notepad",
            "north pad": "notepad",
            "north bad": "notepad",
            "google chrome": "chrome",
        }

    def normalize(self, text: str) -> str:
        normalized = text.lower().strip()

        for wrong, correct in self.replacements.items():
            normalized = normalized.replace(wrong, correct)

        return normalized


speech_normalizer = SpeechNormalizer()