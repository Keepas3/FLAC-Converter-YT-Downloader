import yt_dlp as youtube_dl

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'verbose': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Starting download...")
        ydl.download([url])
        print("Download complete!")

# Example usage
url = 'https://www.youtube.com/watch?v=gcMZ8Aj_ans'
output_path = 'C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs'
download_youtube_video(url, output_path)
