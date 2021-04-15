# Welcome to dword
> An amazing library to create synthetic videos


```
from nbdev import show_doc
from dword.core import DeepWord
```

## Installation

1. Install the dword library

```
pip install dword
```

2. Make sure you have [ffmpeg installed.](https://ffmpeg.org/download.html)

## Quick start

### Step 1: Use api keys to login

Start by [logging into your DeepWord account](https://login.deepword.co/user/signin) and generating API keys

![test_image](images/api_key.png)

Use these keys to login to your account in Python

```python
acc = DeepWord(API_KEY, SECRET_KEY)
```

### Step 2: Start creating videos

**That's it!!!** Now you can start creating videos. We have many options for choosing a video or an audio. Possible pipelines for each is shown below

## Pipelines for videos

The main function in ``dword`` is the ``generate_video`` function. It's what we will use to generate synthetic videos. All we need is a video of the person we want talking and the audio we want them to say.


<h4 id="DeepWord.generate_video" class="doc_header"><code>DeepWord.generate_video</code><a href="https://github.com/deepword18/dword/tree/master/dword/core.py#L219" class="source_link" style="float:right">[source]</a></h4>

> <code>DeepWord.generate_video</code>(**`video`**:`str`, **`audio`**:`str`, **`title`**:`str`=*`None`*)

Generate a synthetic video using a video of a person talking and the audio
   you want them to say. You can check the status of the video using
   ``list_generated_videos`` and download it using ``download_video`` or
   ``download_all_videos``

Args:
    video (str): Video of the person you want talking.
    audio (str): Audio you want the person to say.
    title (str, optional): Optionally provide a title for the output. Defaults to
                           name of the video file.

Raises:
    ValueError: If video or audio don't exist


For the video, we have 3 options
### Option 1: Local video file

You can have a file downloaded locally. In that case you just need to pass the path to the file to the ``generate_video`` function

```python
acc.generate_video('videos/local_vid.mp4', audio, outfile)
```

### Option2: YouTube video

You can use a YouTube video as the input to the generate video function. For this, you will have to first download the YouTube video and then use it as a local video like we did in the example above. For this, we will use the ``download_youtube_video`` function. You can also provide a start_time and an end_time to crop the video before downloading


<h4 id="DeepWord.download_youtube_video" class="doc_header"><code>DeepWord.download_youtube_video</code><a href="https://github.com/deepword18/dword/tree/master/dword/core.py#L162" class="source_link" style="float:right">[source]</a></h4>

> <code>DeepWord.download_youtube_video</code>(**`url`**:`str`, **`types`**:`str`=*`'video'`*, **`start_time`**:`int`=*`None`*, **`end_time`**:`int`=*`None`*)

Download a video from YouTube. You can also donwload an audio and provide start and
   end times to download a trimmed version.

Args:
    url (str): url of the video you want to download.
    types (str, optional): [description]. Defaults to 'video'.
    start_time (int, optional): Start time in seconds. Defaults to None.
    end_time (int, optional): End time in seconds. Defaults to None.

Raises:
    ValueError: If start time is provided but end time is not or the other way round.
    ValueError: If start time is greater than end time.
    ValueError: If end time is greater than the length of the YouTube video.

Returns:
    fname (str): filename of the downloaded video

