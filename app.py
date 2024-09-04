from coqui_TTS.audio_generator import generate_audio_from_text


def generate_avatar():
    print('SadTalker face is generated')


def generate_audio():
    generate_audio_from_text('TTS wav is generated', './output/audio.wav')


if __name__ == '__main__':
    generate_audio()
    generate_avatar()