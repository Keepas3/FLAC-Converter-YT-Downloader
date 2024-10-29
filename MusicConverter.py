from moviepy.editor import *

def convert_mp4_to_flac(mp4_path, flac_path):
    video = VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(flac_path, codec='flac')

mp4_path = "C:\\Users\\Username\\Downloads\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM]\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM] (1080p_24fps_H264-128kbit_AAC).mp4" # copy as path the mp4 file
flac_path = "C:\\Users\\username\OneDrive\\Desktop\\Folder to addSongs\\Sleepwalking.flac"  # Specify where you want the file to go and file name

convert_mp4_to_flac(mp4_path, flac_path)
