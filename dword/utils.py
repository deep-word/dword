# AUTOGENERATED! DO NOT EDIT! File to edit: 01_utils.ipynb (unless otherwise specified).

__all__ = ['to_hhmmss', 'to_secs', 'display_video', 'check_resolution', 'check_fps', 'display_audio',
           'change_audio_format', 'trim_audio']

# Internal Cell
import os
import subprocess
import time
from pathlib import Path
from subprocess import CalledProcessError
from typing import Dict, Union

import cv2
from fastcore.test import *
import imageio
from IPython.display import Audio, Video
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from nbdev.showdoc import *
from pydub import AudioSegment

# Internal Cell
class URLs:
    base = 'https://login.deepword.co:3000/api'
    credits_url = f'{base}/api_get_credits/'
    list_vids_url = f'{base}/list_video_api/'
    txt2speech_url = f'{base}/api_text_to_speech/'
    download_vid_url = f'{base}/api_download_video/'
    download_yt_vid_url = f'{base}/api_download_youtube_video/'
    generate_vid_url = f'{base}/generate_video_api'
    validate_token_url = f'{base}/check_apikey'
    api_get_audio_sample = f'{base}/api_get_audio_sample'
    api_get_video_actors = f'{base}/api_get_video_actors'
    trim_video = 'https://youtube.deepword.co:5000/api_trim_video'

# Internal Cell
class TextDicts:
    langs = ["arabic", "bengali", "chinese", "czech", "danish", "dutch", "english_aus", "english_ind",
             "english_uk", "english_us", "filipino", "finnish", "french_canada", "french", "german",
             "greek", "gujarati", "hindi", "hungarian", "indonesian", "italian", "japanese", "kannada",
             "korean", "malayalam", "mandarin", "mandarin_taiwan", "norwegian", "polish", "portuguese_brazil", "portuguese",
             "russian", "slovak", "spanish", "swedish", "tamil", "telugu", "thai", "turkish", "ukrainian"]

    codes = ["ar-XA", "bn-IN", "yue-HK", "cs-CZ", "da-DK", "nl-NL", "en-AU", "en-IN", "en-GB",
             "en-US", "fil-PH", "fi-FI", "fr-CA", "fr-FR", "de-DE", "el-GR", "gu-IN", "hi-IN",
             "hu-HU", "id-ID", "it-IT", "ja-JP", "kn-IN", "ko-KR", "ml-IN", "cmn-CN", "cmn-TW", "nb-NO",
             "pl-PL", "pt-BR", "pt-PT", "ru-RU", "sk-SK", "es-ES", "sv-SE", "ta-IN", "te-IN",
             "th-TH", "tr-TR", "uk-UA", "vi-VN"]

    lang2code = dict(zip(langs, codes))

    speakers = {
        "arabic":  ["ar-XA-Wavenet-A FEMALE","ar-XA-Wavenet-B MALE","ar-XA-Wavenet-C MALE","ar-XA-Standard-A FEMALE","ar-XA-Standard-B MALE","ar-XA-Standard-C MALE","ar-XA-Standard-D FEMALE"],
        "bengali": ["bn-IN-Standard-A FEMALE","bn-IN-Standard-B MALE"],
        "chinese": ["yue-HK-Standard-A FEMALE","yue-HK-Standard-B MALE","yue-HK-Standard-C FEMALE","yue-HK-Standard-D MALE"],
        "czech": ["cs-CZ-Wavenet-A FEMALE","cs-CZ-Standard-A FEMALE"],
        "danish": ["da-DK-Wavenet-A FEMALE","da-DK-Wavenet-C MALE","da-DK-Wavenet-D FEMALE","da-DK-Wavenet-E FEMALE","da-DK-Standard-A FEMALE","da-DK-Standard-C MALE","da-DK-Standard-D FEMALE","da-DK-Standard-E FEMALE"],
        "dutch": ["nl-NL-Wavenet-A FEMALE","nl-NL-Wavenet-B MALE","nl-NL-Wavenet-C MALE","nl-NL-Wavenet-D FEMALE","nl-NL-Wavenet-E FEMALE","nl-NL-Standard-A FEMALE","nl-NL-Standard-B MALE","nl-NL-Standard-C MALE","nl-NL-Standard-D FEMALE","nl-NL-Standard-E FEMALE"],
        "english_aus": ["en-AU-Wavenet-A FEMALE","en-AU-Wavenet-B MALE","en-AU-Wavenet-C FEMALE","en-AU-Wavenet-D MALE","en-AU-Standard-A FEMALE","en-AU-Standard-B MALE","en-AU-Standard-C FEMALE","en-AU-Standard-D MALE"],
        "english_ind": ["en-IN-Wavenet-A FEMALE","en-IN-Wavenet-B MALE","en-IN-Wavenet-C MALE","en-IN-Wavenet-D FEMALE","en-IN-Standard-A FEMALE","en-IN-Standard-B MALE","en-IN-Standard-C MALE","en-IN-Standard-D FEMALE"],
        "english_uk": ["en-GB-Wavenet-A FEMALE","en-GB-Wavenet-B MALE","en-GB-Wavenet-C FEMALE","en-GB-Wavenet-D MALE","en-GB-Wavenet-F FEMALE","en-GB-Standard-A FEMALE","en-GB-Standard-B MALE","en-GB-Standard-C FEMALE","en-GB-Standard-D MALE","en-GB-Standard-F FEMALE"],
        "english_us": ["en-US-Wavenet-A MALE","en-US-Wavenet-B MALE","en-US-Wavenet-C FEMALE","en-US-Wavenet-D MALE","en-US-Wavenet-E FEMALE","en-US-Wavenet-F FEMALE","en-US-Wavenet-G FEMALE","en-US-Wavenet-H FEMALE","en-US-Wavenet-I MALE","en-US-Wavenet-J MALE" ,"en-US-Standard-B MALE","en-US-Standard-C FEMALE","en-US-Standard-D MALE","en-US-Standard-E FEMALE","en-US-Standard-G FEMALE","en-US-Standard-H FEMALE","en-US-Standard-I MALE","en-US-Standard-J MALE"],
        "filipino": ["fil-PH-Wavenet-A FEMALE","fil-PH-Wavenet-B FEMALE","fil-PH-Wavenet-C MALE","fil-PH-Wavenet-D MALE","fil-PH-Standard-A FEMALE","fil-PH-Standard-B FEMALE","fil-PH-Standard-C MALE","fil-PH-Standard-D MALE"],
        "finnish": ["fi-FI-Wavenet-A FEMALE","fi-FI-Standard-A FEMALE"],
        "french_canada": ["fr-CA-Wavenet-A FEMALE","fr-CA-Wavenet-B MALE","fr-CA-Wavenet-C FEMALE","fr-CA-Wavenet-D MALE","fr-CA-Standard-A FEMALE","fr-CA-Standard-B MALE","fr-CA-Standard-C FEMALE","fr-CA-Standard-D MALE"],
        "french": ["fr-FR-Wavenet-A FEMALE","fr-FR-Wavenet-B MALE","fr-FR-Wavenet-C FEMALE","fr-FR-Wavenet-D MALE","fr-FR-Wavenet-E FEMALE","fr-FR-Standard-A FEMALE","fr-FR-Standard-B MALE","fr-FR-Standard-C FEMALE","fr-FR-Standard-D MALE","fr-FR-Standard-E FEMALE"],
        "german": ["de-DE-Wavenet-A FEMALE","de-DE-Wavenet-B MALE","de-DE-Wavenet-C FEMALE","de-DE-Wavenet-D MALE","de-DE-Wavenet-E MALE","de-DE-Wavenet-F FEMALE","de-DE-Standard-A FEMALE","de-DE-Standard-B MALE","de-DE-Standard-E MALE","de-DE-Standard-F FEMALE"],
        "greek": ["el-GR-Wavenet-A FEMALE","el-GR-Standard-A FEMALE"],
        "gujarati": ["gu-IN-Standard-A FEMALE","gu-IN-Standard-B MALE"],
        "hindi": ["hi-IN-Wavenet-A FEMALE","hi-IN-Wavenet-B MALE","hi-IN-Wavenet-C MALE","hi-IN-Wavenet-D FEMALE","hi-IN-Standard-A FEMALE","hi-IN-Standard-B MALE","hi-IN-Standard-C MALE","hi-IN-Standard-D FEMALE"],
        "hungarian": ["hu-HU-Wavenet-A FEMALE","hu-HU-Standard-A FEMALE"],
        "indonesian": ["id-ID-Wavenet-A FEMALE","id-ID-Wavenet-B MALE","id-ID-Wavenet-C MALE","id-ID-Wavenet-D FEMALE","id-ID-Standard-A FEMALE","id-ID-Standard-B MALE","id-ID-Standard-C MALE","id-ID-Standard-D FEMALE"],
        "italian": ["it-IT-Wavenet-A FEMALE","it-IT-Wavenet-B FEMALE","it-IT-Wavenet-C MALE","it-IT-Wavenet-D MALE","it-IT-Standard-A FEMALE","it-IT-Standard-B FEMALE","it-IT-Standard-C MALE","it-IT-Standard-D MALE"],
        "japanese": ["ja-JP-Wavenet-A FEMALE","ja-JP-Wavenet-B FEMALE","ja-JP-Wavenet-C MALE","ja-JP-Wavenet-D MALE","ja-JP-Standard-A FEMALE","ja-JP-Standard-B FEMALE","ja-JP-Standard-C MALE","ja-JP-Standard-D MALE"],
        "kannada": ["kn-IN-Standard-A FEMALE","kn-IN-Standard-B MALE"],
        "korean": ["ko-KR-Wavenet-A FEMALE","ko-KR-Wavenet-B FEMALE","ko-KR-Wavenet-C MALE","ko-KR-Wavenet-D MALE","ko-KR-Standard-A FEMALE","ko-KR-Standard-B FEMALE","ko-KR-Standard-C MALE","ko-KR-Standard-D MALE"],
        "malayalam": ["ml-IN-Standard-A FEMALE","ml-IN-Standard-B MALE"],
        "mandarin": ["cmn-CN-Wavenet-A FEMALE","cmn-CN-Wavenet-B MALE","cmn-CN-Wavenet-C MALE","cmn-CN-Wavenet-D FEMALE", "cmn-CN-Standard-A FEMALE","cmn-CN-Standard-B MALE","cmn-CN-Standard-C MALE","cmn-CN-Standard-D FEMALE"],
        "mandarin_taiwan": ["cmn-TW-Wavenet-A FEMALE","cmn-TW-Wavenet-B MALE","cmn-TW-Wavenet-C MALE", "cmn-TW-Standard-A FEMALE","cmn-TW-Standard-B MALE","cmn-TW-Standard-C MALE"],
        "norwegian": ["nb-NO-Wavenet-A FEMALE","nb-NO-Wavenet-B MALE","nb-no-Wavenet-E FEMALE","nb-NO-Wavenet-C FEMALE","nb-NO-Wavenet-D MALE","nb-NO-Standard-A FEMALE","nb-NO-Standard-B MALE","nb-NO-Standard-C FEMALE","nb-NO-Standard-D MALE","nb-no-Standard-E FEMALE"],
        "polish": ["pl-PL-Wavenet-A FEMALE","pl-PL-Wavenet-B MALE","pl-PL-Wavenet-C MALE","pl-PL-Wavenet-D FEMALE","pl-PL-Wavenet-E FEMALE","pl-PL-Standard-A FEMALE","pl-PL-Standard-B MALE","pl-PL-Standard-C MALE","pl-PL-Standard-D FEMALE","pl-PL-Standard-E FEMALE"],
        "portuguese_brazil": ["pt-BR-Wavenet-A FEMALE","pt-BR-Standard-A FEMALE"],
        "portuguese": ["pt-PT-Wavenet-A FEMALE","pt-PT-Wavenet-B MALE","pt-PT-Wavenet-C MALE","pt-PT-Wavenet-D FEMALE","pt-PT-Standard-A FEMALE","pt-PT-Standard-B MALE","pt-PT-Standard-C MALE","pt-PT-Standard-D FEMALE"],
        "russian": ["ru-RU-Wavenet-A FEMALE","ru-RU-Wavenet-B MALE","ru-RU-Wavenet-C FEMALE","ru-RU-Wavenet-D MALE","ru-RU-Wavenet-E FEMALE","ru-RU-Standard-A FEMALE","ru-RU-Standard-B MALE","ru-RU-Standard-C FEMALE","ru-RU-Standard-D MALE","ru-RU-Standard-E FEMALE"],
        "slovak": ["sk-SK-Wavenet-A FEMALE","sk-SK-Standard-A FEMALE"],
        "spanish": ["es-ES-Wavenet-B MALE","es-ES-Standard-A FEMALE","es-ES-Standard-B MALE"],
        "swedish": ["sv-SE-Wavenet-A FEMALE","sv-SE-Standard-A FEMALE"],
        "tamil": ["ta-IN-Standard-A FEMALE","ta-IN-Standard-B MALE"],
        "telugu": ["te-IN-Standard-A FEMALE","te-IN-Standard-B MALE"],
        "thai": ["th-TH-Standard-A FEMALE"],
        "turkish": ["tr-TR-Wavenet-A FEMALE","tr-TR-Wavenet-B MALE","tr-TR-Wavenet-C FEMALE","tr-TR-Wavenet-D FEMALE","tr-TR-Wavenet-E MALE","tr-TR-Standard-A FEMALE","tr-TR-Standard-B MALE","tr-TR-Standard-C FEMALE","tr-TR-Standard-D FEMALE","tr-TR-Standard-E MALE"],
        "ukrainian": ["uk-UA-Wavenet-A FEMALE","uk-UA-Standard-A FEMALE"],
        "vietnamese": ["vi-VN-Wavenet-A FEMALE","vi-VN-Wavenet-B MALE","vi-VN-Wavenet-C FEMALE","vi-VN-Wavenet-D MALE","vi-VN-Standard-A FEMALE FEMALE","vi-VN-Standard-B MALE","vi-VN-Standard-C FEMALE","vi-VN-Standard-D MALE"]
    }

# Cell
def to_hhmmss(x: int) -> str:
    """Convert time from secs (int) to hh:mm:ss (str).
    """
    if not x >= 0: raise Exception(f'seconds cannot be negative, got {x}')
    return time.strftime("%H:%M:%S", time.gmtime(x))

# Cell
def to_secs(x: str) -> int:
    """Convert time from hh:mm:ss (str) format to seconds (int).
    """
    h, m, s = x.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# Internal Cell
def _remove_duplicate(outfile):
    if Path(outfile).exists(): os.remove(f'{outfile}')

# Internal Cell
def _exists(x): return Path(x).exists()

# Cell
def display_video(video): return Video(video, height = 400, width = 400)

# Cell
def check_resolution(video: Union[str, Path]) -> Dict:
    """Check the resolution of a video.
    """
    try:
        vid = cv2.VideoCapture(video)
        h, w = vid.get(cv2.CAP_PROP_FRAME_HEIGHT), vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        return {'height': int(h), 'width': int(w)}
    except Exception as e:
        raise ValueError(e)

# Cell
def check_fps(video: Union[str, Path], round_res = False) -> float:
    """Get the fps of a video
    """
    reader = imageio.get_reader(video)
    fps = reader.get_meta_data()['fps']
    return fps if not round_res else round(fps)

# Cell
def display_audio(audio): return Audio(audio)

# Cell
def change_audio_format(audio: Union[str, Path], outfile: Union[str, Path]) -> None:
    """Change the format of audio file. Example, converting mp3 to wav. Works with
       all formats supported by ffmpeg.
    """
    _remove_duplicate(outfile)

    audio, outfile = Path(audio), Path(outfile)
    ext, o_ext = audio.suffix[1:], outfile.suffix[1:]
    f = AudioSegment.from_file(audio, ext)
    f.export(outfile, format = o_ext)

# Cell
def trim_audio(audio: Union[str, Path], start_time: int, end_time: int, outfile: Union[str, Path] = 'trimmed_audio.mp3') -> None:
    """Trim an audio file. Start and end times are in seconds. Works with all formats supported by ffmpeg.
    """
    _remove_duplicate(outfile)

    audio, outfile = Path(audio), Path(outfile)
    ext, o_ext = audio.suffix[1:], outfile.suffix[1:]
    f = AudioSegment.from_file(audio, ext)

    start_time = start_time * 1000
    end_time = end_time * 1000

    f = f[start_time:end_time]
    f.export(outfile, format = o_ext)
    return outfile