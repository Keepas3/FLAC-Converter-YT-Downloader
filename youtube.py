from pytubefix import YouTube

link = input ("Enter Link")
yt = YouTube(link)
audio_stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
audio_stream.download()
print("DONE")
