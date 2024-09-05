from coqui_TTS.audio_generator import generate_audio_from_text


def generate_avatar():
    args = inference.set_default_args()

    args.source_image = "input\face1.png"
    args.driven_audio = 'input\Thank.wav'
    args.init_path = 'SadTalker'
    args.enhancer = 'gfpgan'

    sad_talker_inference(args)


def generate_audio():
    generate_audio_from_text('TTS wav is generated', './output/audio.wav')


if __name__ == '__main__':
    generate_audio()
    generate_avatar()