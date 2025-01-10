import os
from flask import Flask, request, redirect, url_for, render_template
from moviepy.editor import VideoFileClip, AudioFileClip
import pytubefix
from pytubefix import YouTube

Server = Flask(__name__)

UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER')
Server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            stream.download(output_path)
        else:
            raise Exception("No MP4 stream available")
    except pytubefix.exceptions.VideoUnavailable:
        raise Exception("Video unavailable")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

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

@Server.route('/')
def home():
    return render_template('Converter.html')

@Server.route('/convert', methods=['POST'])
def convert():
    mp4_path = None

    # Handle YouTube URL
    youtube_url = request.form.get('youtube_url')
    print(youtube_url + "WHAWHSHWJHWJHDR")
    if youtube_url:
        mp4_path = os.path.join(UPLOAD_FOLDER, 'downloaded_video.mp4')
        try:
            download_youtube_video(youtube_url, UPLOAD_FOLDER)
            message = f"Conversion Complete! Youtube Video saved at {mp4_path}"
            return redirect(url_for('result', message=message))
        except Exception as e:
            return f"Failed to download video: {str(e)}"

    # Handle MP4 file upload
    if 'mp4_file' in request.files and request.files['mp4_file'].filename != '':
        file = request.files['mp4_file']
        mp4_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(mp4_path)

    if not mp4_path:
        return "No video provided"

    title = extract_title_from_path(mp4_path)
    flac_path = os.path.join(OUTPUT_FOLDER, f"{title}.flac")

    try:
        convert_video_to_flac(mp4_path, flac_path)
        message = f"Conversion Complete! FLAC file saved at {flac_path}"
    except Exception as e:
        message = f"Conversion failed: {str(e)}"

    return redirect(url_for('result', message=message))

def extract_title_from_path(path):
    base_name = os.path.basename(path)
    title, _ = os.path.splitext(base_name)
    return title

@Server.route('/result')
def result():
    message = request.args.get('message', '')
    return render_template('Result.html', message=message)

if __name__ == '__main__':
    Server.run(debug=True)
