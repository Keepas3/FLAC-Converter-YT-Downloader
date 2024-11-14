from flask import Flask, request, render_template
from moviepy.editor import *
import os

Server = Flask(__name__)

def convert_video_to_flac(video_path, flac_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(flac_path, codec='flac')

@Server.route('/')
def home():
    return render_template('Converter.html')

@Server.route('/convert', methods=['POST'])
def convert(): 
    mp4_path = request.form['mp4_path']
    mp4_path = mp4_path.replace('"', '').replace("'", "")
    
    title = extract_title_from_path(mp4_path)
    flac_path = f"C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.flac"
    
    convert_video_to_flac(mp4_path, flac_path)
    
    return f"Conversion complete! FLAC file saved at {flac_path}"

def extract_title_from_path(path):
    base_name = os.path.basename(path)
    title, _ = os.path.splitext(base_name)
    return title

if __name__ == '__main__':
    Server.run(debug=True)
