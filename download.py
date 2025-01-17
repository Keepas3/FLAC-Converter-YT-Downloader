from pytubefix import YouTube

link = input("Enter Link: ")
yt = YouTube(link)
vid = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
vid.download()
print("DONE")
