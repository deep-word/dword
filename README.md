# Welcome to dword
> An amazing library to create synthetic videos


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


We hope you enjoy this project

## Installation

1. Install the dword library

```
pip install dword
```

2. Make sure you have [ffmpeg installed.](https://ffmpeg.org/download.html)

## Quick start

You can use the `generate_video` function to create a synthetic video

```python
generate_video('Anna.mp4', 'audio.mp3', 'myoutput.mp4')
```

    Successfully generated video!

