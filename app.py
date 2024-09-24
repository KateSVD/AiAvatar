from coqui_TTS.audio_generator import generate_audio_from_text
import sys
import os
sys.path.append('C:\AI\AiAvatar\SadTalker')

import inference

def generate_avatar():
    os.chdir('SadTalker')
    args = inference.set_default_args()
    args.driven_audio = '../input/audio.wav'
    args.source_image = '../input/face1.png'
    inference.sad_talker_inference(args)

def generate_audio():
    generate_audio_from_text('Hello audio generator', './input/audio.wav')

if __name__ == '__main__':
    generate_audio()
    generate_avatar()