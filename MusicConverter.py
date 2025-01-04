from moviepy.editor import *
from pytube import YouTube
import os
import requests
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# output_path ="C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs"
# Not used as of now, replaced by Server.py class



# video_path = "C:\\Users\\fungb\\Downloads\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM]\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM] (1080p_24fps_H264-128kbit_AAC).mp4"
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

amr_path = "C:\\Users\\fungb\\Downloads\\Quiet Beat.amr"
title = extract_title_from_path(amr_path)
convert_amr_to_wav(amr_path,f"C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.wav" )

files_to_Convert = [
    "C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs\\Age of Empires Rise of Rome Music 6 (480p_30fps_H264-128kbit_AAC).mp4",
    "C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs\\Age of Empires Rise of Rome Music 2\\Age of Empires Rise of Rome Music 2 (480p_30fps_H264-128kbit_AAC).mp4"
]
# colorama_init
# for video_path in files_to_Convert: 
#     title = extract_title_from_path(video_path)
#     flac_path = f"C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.flac" 
#     print( Fore.RED + f"Title: {title}") 
#     convert_video_to_flac(video_path, flac_path)
#     print(Fore.BLUE + f"Converted output from {video_path} to {flac_path}")