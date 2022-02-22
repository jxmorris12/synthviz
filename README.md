# synthviz

`synthviz` is a library for creating visualizations of piano-playing from MIDI files. The videos look like this:

<video src="https://replicate.com/api/models/jxmorris12/piano-transcription/files/85c361bf-41cb-4a33-bc70-3d195cf23b90/output.mp4" width="640"/>

Right now, synthviz just provides a Python API. Command-line API is hopefully coming soon!

## Requirements

### system requirements

You'll need to install a couple of tools that make rendering this video possible:

1. [ffmpeg](https://ffmpeg.org) (creates video from audio and image video frames) - on Ubuntu, `sudo apt-get install ffmpeg`
2. [timidity](http://timidity.sourceforge.net/install.html) (synthesizes piano audio from MIDI) - on Ubuntu, `sudo apt-get install timidity`

### python package requirements

Install this package via `pypi`: 

```bash
pip install synthviz
```

## Usage

You can use synthviz through the Python API:

```python
from synthviz import create_video

create_video('river.midi') # provide str path of MIDI file
```

## Options

The `create_video` function provides a lot of of options:

```python
def create_video(input_midi: str, 
		video_filename = "output.mp4",
		image_width	= 1280,
		image_height = 720,
		black_key_height = 2/3,
		falling_note_color = [75, 105, 177], # default: darker blue
		pressed_key_color = [197, 208, 231], # default: lighter blue
		vertical_speed = 1/4,
		fps = 20
	) 
```

- `input_midi` (str): path to MIDI file
- `video_filename` (str): path to output video, synthviz will write the video here
- `image_width` (int): width of output video in px
- `image_height` (int): height of output video in px
- `black_key_height` (float): height of black keys as a percentage of piano height 
- `falling_note_color` (Tuple[int]): color of falling keys in video, list of three RGB integers
- `pressed_key_color` (Tuple[int]): color of pressed-down keys in video, list of three RGB integers
- `vertical_speed` (float): the speed of the falling keys, fraction measured as main-image-heights per second
- `fps` (int): frames-per-second of output video


## Creating video from raw audio

With the help of the [`piano_transcription_inference`](https://github.com/qiuqiangkong/piano_transcription_inerence) library, you can make a cool video directly from raw audio! 

First, install that library via `pip install piano_transcription_inference`. Then run the following code:

```python
import librosa
import os
import pathlib

from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
from synthviz import create_video

audio_input = 'my_audio.mp3'
midi_intermediate_filename = 'transcription.mid'
video_filename = 'output.mp4'

transcriptor = PianoTranscription(device='cuda', checkpoint_path='./model.pth')
audio, _ = librosa.core.load(str(audio_input), sr=sample_rate)
transcribed_dict = transcriptor.transcribe(audio, midi_intermediate_filename)
create_video(input_midi=midi_intermediate_filename, video_filename=video_filename)
```

# Credits

The synthviz library was originall adapted from [this blog post](https://pappubahry.com/misc/piano_diaries/synthesia/), 
"Making Synthesia-style videos in Ubuntu", written by David Barry. Thanks David!
