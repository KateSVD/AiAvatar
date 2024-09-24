import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"


def generate_audio_from_text(text, audio_path):
    tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text, file_path=audio_path)
