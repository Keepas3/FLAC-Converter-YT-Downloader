from flask import Flask, request, redirect, url_for, render_template
from moviepy.editor import *
import os

Server = Flask(__name__)
Server.config['UPLOAD_FOLDER'] = 'uploads'
Server.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size

def convert_video_to_flac(video_path, flac_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
    except Exception as e: 
        print(f"Error processing video file: {e}") 
        try: 
            audio = AudioFileClip(video_path) 
        except Exception as e: 
            print(f"Error processing audio file: {e}") 
            raise e 
        
    try: 
        audio.write_audiofile(flac_path, codec='flac') 
        print(f"Conversion complete! FLAC file saved at {flac_path}") 

    except Exception as e: 
        print(f"Error writing audio file: {e}") 
        raise e


@Server.route('/')
def home():
    return render_template('Converter.html')

@Server.route('/convert', methods=['POST'])
def convert():
    print("Request Content-Type:", request.content_type) 
    print("Request Files:", request.files) 
    print("Request Form:", request.form)
    if 'mp4_file' not in request.files:
        print("No file part detected")
        return "No file part", 400  # Return a bad request error if no file part is found
    file = request.files['mp4_file']
    if file.filename == '':
        print("No selected file detected")
        return "No selected file", 400  # Return a bad request error if no file is selected
    print("File received:", file.filename)
    if file:
        file_path = os.path.join(Server.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        title = extract_title_from_path(file.filename)
        flac_path = "C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.wav"
       # flac_path = os.path.join(Server.config['UPLOAD_FOLDER'], f"{title}.flac")

        try:
            convert_video_to_flac(file_path, flac_path)
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
    return render_template('Result.html')

if __name__ == '__main__':
    if not os.path.exists(Server.config['UPLOAD_FOLDER']):
        os.makedirs(Server.config['UPLOAD_FOLDER'])
    Server.run(debug=True)



# @Server.route('/convert', methods=['POST']) # maps the /convert URL to convert function
# def convert(): 
#     mp4_path = request.form['mp4_path'] # retrieves the value of the text field typed in by the user
#     mp4_path = mp4_path.replace('"', '').replace("'", "") #replaces any quotes 
    
#     title = extract_title_from_path(mp4_path)
# #    flac_path = f"C:\\Users\\bryan\\OneDrive\\Desktop\\New folder (2)\\{title}.flac"
#     flac_path = f"C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\{title}.flac"
    
#     try:
#         convert_video_to_flac(mp4_path, flac_path)
#         message = f"Conversion Complete! FLAC file saved at {flac_path}"
#     except Exception as e:
#         message = f"Conversion failed: {str(e)}"

#     print("Rendering template with message:", message)
#     return redirect(url_for('result', message = message))
