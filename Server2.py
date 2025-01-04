import os
from flask import Flask, request, redirect, url_for, render_template
from moviepy.editor import VideoFileClip, AudioFileClip

Server2 = Flask(__name__)

UPLOAD_FOLDER = 'C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs'
OUTPUT_FOLDER = 'C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs'

def convert_video_to_flac(video_path, flac_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(flac_path, codec='flac')
    except KeyError:
        audio = AudioFileClip(video_path)
        audio.write_audiofile(flac_path, codec='flac')
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

@Server2.route('/')
def home():
    return render_template('Converter.html')

@Server2.route('/convert', methods=['POST'])
def convert():
    if 'mp4_file' not in request.files:
        return "No file part"
    file = request.files['mp4_file']
    if file.filename == '':
        return "No selected file"
    if file:
        mp4_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(mp4_path)
        
        title = extract_title_from_path(mp4_path)
        flac_path = os.path.join(OUTPUT_FOLDER, f"{title}.flac")
        
        try:
            convert_video_to_flac(mp4_path, flac_path)
            message = f"Conversion Complete! FLAC file saved at {flac_path}"
        except Exception as e:
            message = f"Conversion failed: {str(e)}"
        
        print("Rendering template with message:", message)
        return redirect(url_for('result', message=message))

def extract_title_from_path(path):
    base_name = os.path.basename(path)
    title, _ = os.path.splitext(base_name)
    return title

@Server2.route('/result')
def result():
    message = request.args.get('message', '')
    return render_template('Result.html', message=message)

if __name__ == '__main__':
    Server2.run(debug=True)
