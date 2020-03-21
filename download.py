import pytube

video = input("Pase the url here: ")

video_url = video # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/home/king/Videos/ccna_youtube_turtorial') # path, where to video download.



