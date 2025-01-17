from moviepy.editor import *
from pytube import YouTube
import os
import requests
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


# Not used as of now, replaced by Server.py class



#convert_video_to_flac(video_path, flac_path)

def convert_video_to_flac(video_path, flac_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(flac_path, codec='flac')

def convert_amr_to_wav(amr_path, wav_path):
    audio = AudioFileClip(amr_path)
    audio.write_audiofile(wav_path, codec = 'pcm_s16le')


def extract_title_from_path(path): # Extracts the base name and removes the extension 
    base_name = os.path.basename(path) 
    title, _ = os.path.splitext(base_name) 
    return title
amr_path = ""
title = extract_title_from_path(amr_path)
convert_amr_to_wav("","")
