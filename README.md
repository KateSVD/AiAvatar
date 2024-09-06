# AiAvatar
Generates talking head (avatar) based on an input face picture and text. Realtime. Uses popular AI models ([SadTalker](https://github.com/OpenTalker/SadTalker),TTS).

## Setup
- Install Anaconda, Python and git.
- Create Anaconda environment _avatar_ and specify Python version 3.8.
```
cd AiAvatar
conda create -n avatar python=3.8
```
- Activate conda environment:
```
conda activate avatar
```
If it doesn't work, go to Anaconda Navigator and activate environment manually. Run terminal from Anaconda Navigator and execute all commands there.

- Install ffmpeg, torch and requirements
```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

conda install ffmpeg
```
- Create folder "checkpoints" in AiAvatar/SadTalker. Download [checkpoints](https://drive.google.com/file/d/1gwWh45pF7aelNP_P78uDJL8Sycep-K7j/view) to this folder.

- Try running script using example audio and face image from folder AiAvatar/input.
```
python inference.py --driven_audio C:\AI\AiAvatar\input\Thank.wav --source_image C:\AI\AiAvatar\input\face1.png --enhancer gfpgan
```
- Wait for gfpgan download and video generation, folder AiAvatar/results will contain video.

### Setup coqui/TTS for sound generation
- Install tts
```
python install tts
```

Use generated file placed in the ./output directory as input for the SadTalker.
