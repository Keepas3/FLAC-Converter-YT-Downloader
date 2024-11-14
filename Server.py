from flask import Flask, request, render_template
from moviepy.editor import *
import os

Server = Flask(__name__)

def convert_video_to_flac(video_path, flac_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
    except KeyError:
        audio = AudioFileClip(video_path)
    audio.write_audiofile(flac_path, codec='flac')

@Server.route('/')
def home(): # Tells the server to render the home page or the Converter.html when they type in the URL
    return render_template('Converter.html')

@Server.route('/convert', methods=['POST']) # maps the /convert URL to convert function
def convert(): 
    mp4_path = request.form['mp4_path'] # retrieves the value of the text field typed in by the user
    mp4_path = mp4_path.replace('"', '').replace("'", "") #replaces any quotes 
    
    title = extract_title_from_path(mp4_path)
  #  flac_path = f"C:\\Users\\bryan\\OneDrive\\Desktop\\New folder (2)\\{title}.flac"
    flac_path = f"C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.flac"
    
    try:
        convert_video_to_flac(mp4_path, flac_path)
        message = f"Conversion Complete! FLAC file saved at {flac_path}"
    except Exception as e:
        message = f"Conversion failed: {str(e)}"

    print("Rendering template with message:", message)
    return render_template('Result.html')
    #return f"Conversion complete! FLAC file saved at {flac_path}"

def extract_title_from_path(path):
    base_name = os.path.basename(path)
    title, _ = os.path.splitext(base_name)
    return title

if __name__ == '__main__':
    Server.run(debug=True)
