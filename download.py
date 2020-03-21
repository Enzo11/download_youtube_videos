import pytube

video = input("Pase the url here: ")

video_url = video # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.get_highest_resolution().download('/home/king/Videos/mytool_download_youtube_video')
#video.download('/home/king/Videos/mytool_download_youtube_video') # path, where to video download.



#YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
