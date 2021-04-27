# Welcome to dword
> An amazing library to create synthetic videos


```python
import os

from nbdev import show_doc
from dword.core import DeepWord
```

## Installation

Install the dword library

```
pip install dword
```

## Quick start

### Step 1: Use api keys to login

Start by [logging into your DeepWord account](https://login.deepword.co/user/signin) and generating API keys

![test_image](images/api_key.png)

Use these keys to login to your account in Python

```python
from dword.core import DeepWord
```

```python
acc = DeepWord(API_KEY, SECRET_KEY)
```

    login successful


### Step 2: Start creating videos
{% include tip.html content='That&#8217;s it!!!!' %}
Now you can start creating synthetic videos. All you need is a video of the person talking and the audio you want them to say.

```python
acc.generate_video('Anna.mp4', 'my_audio.mp3', title = 'first_deepword_video.mp4')
```

    Generating video. This will take a few minutes.





    {'status': True,
     'message': 'Your video has been added to the queue for processing. Please check back in 10-15 minutes',
     'url': 'https://staging.deepword.co/video/u5miip0ko0dcei2'}



{% include important.html content='The video can take a few minutes to generate. You can find the status of the video by retrieving a list of all videos on your account' %}

```python
acc.list_videos()[-1]
```




    {'email': 'blablabla@yopmail.com',
     'thumbnail': 'video_u5miip0ko0dcei2.mp4',
     'title': 'first_deepword_video.mp4',
     'video_url': 'https://videos-deep-word123.s3.us-east-2.amazonaws.com/output_data/u5miip0ko0dcei2.mp4',
     'video_duration': '30.0000',
     'video_id': 'u5miip0ko0dcei2',
     'generate_date': '2021-04-27T18:34:32.000Z',
     'output_status': 'Queued'}



Once the status changes from 'Queued' to 'Completed' you can either use `acc.download_video` or `acc.download_youtube_video` to download your video.
