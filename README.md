# Welcome to dword
> An amazing library to create synthetic videos


## Installation

Install the dword library

```python
pip install dword
```

Make sure you have [ffmpeg installed](https://ffmpeg.org/download.html).

## Quick start

### Step 1: Use api keys to login

Start by [logging into your DeepWord account](https://login.deepword.co/user/signin) and generating API keys

![test_image](images/api_key.png)

Use these keys to login to your DeepWord account via the Python api

```
from dword.core import DeepWord
```

```
acc = DeepWord(API_KEY, SECRET_KEY)
```

    login successful


Now, make sure that you have enough credits available to generate synthetic videos.

```
acc.available_credits
```




    237



### Step 2: Start creating videos

**That's it!!!!**

You can now start creating synthetic videos. All you need is a video of the person talking and the audio you want them to say. In this quick start tutorial, we will use a video and audio we already have. 

To learn more about different ways to use video and audio, refer our [tutorial here](https://deep-word.github.io/dword/tutorials.input_types).

```
acc.generate_video('Anna.mp4', 'my_audio.mp3', title = 'first_deepword_video')
```




    {'status': True,
     'message': 'Your video has been added to the queue for processing. Please check back in 10-15 minutes',
     'url': 'https://login.deepword.co/video/b47y6adtqkkqzdycim'}



{% include important.html content='The video can take a few minutes to generate. You can find the status of the video by retrieving a list of all videos on your account' %}

```
acc.list_videos()[-1]
```




    {'email': 'blablabla@yopmail.com',
     'thumbnail': 'thubnail-b47y6abrm3kqbqc28t.png',
     'title': 'Noelle',
     'video_url': 'https://videos-deep-word123.s3.us-east-2.amazonaws.com/output_data/b47y6abrm3kqbqc28t.mp4',
     'video_duration': '53.952',
     'video_id': 'b47y6abrm3kqbqc28t',
     'generate_date': '2021-06-25T02:43:03.000Z',
     'output_status': 'Complete'}



Once the status changes from 'Queued' to 'Completed' you can either use `acc.download_video` or `acc.download_all_videos` to download your video.

```
acc.download_all_videos()
```
