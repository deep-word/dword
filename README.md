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

Also make sure you have enough credits available in your account to generate videos. You will use these keys to login to your DeepWord account

```
from dword.core import DeepWord
```

```
acc = DeepWord(API_KEY, SECRET_KEY)
```

    login successful


### Step 2: Start creating videos

**That's it!!!!**

You can now start creating synthetic videos. All you need is a video of the person talking and the audio you want them to say. In this quick start tutorial, we will use a video and audio we already have. To learn more about different ways to use video and audio, refer the tutorials tab

```
acc.generate_video('Anna.mp4', 'my_audio.mp3', title = 'first_deepword_video.mp4')
```

    Generating video. This will take a few minutes.





    {'status': True,
     'message': 'Your video has been added to the queue for processing. Please check back in 10-15 minutes',
     'url': 'https://staging.deepword.co/video/u5miip0ko0dcei2'}



{% include important.html content='The video can take a few minutes to generate. You can find the status of the video by retrieving a list of all videos on your account' %}

```
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
