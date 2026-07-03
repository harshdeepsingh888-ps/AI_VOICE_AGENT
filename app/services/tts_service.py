import asyncio
import edge_tts
import pygame


class TTSService:
    def __init__(self):
        self.voice = "en-US-GuyNeural"
        pygame.mixer.init()

    async def text_to_speech(self, text):
        output_file = "response.mp3"

        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        # Release the file after playback
        pygame.mixer.music.unload()


tts_service = TTSService()