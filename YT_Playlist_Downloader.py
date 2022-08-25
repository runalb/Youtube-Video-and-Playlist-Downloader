from pytube import YouTube, Playlist

pl_url = input("Enter YT Playlist URL: ")
pl = Playlist(pl_url)
print(f'\n Playlist Title: {pl.title}')

for yt_video_url in pl.video_urls:
	
	ytv = YouTube(yt_video_url)
	print(f'\n Video Title: {ytv.title}')
	print(f' Video URL: {yt_video_url}')

	ytv_streams = ytv.streams.all()
	ytv_streams_li = list((enumerate(ytv_streams)))

	print("\n Stream lists:")
	for stream in ytv_streams_li:
		print(stream)
	print()

	strm_no = int(input("Enter stream no: "))

	print(f' Downloading...:\n {ytv_streams[strm_no]}')
	ytv_streams[strm_no].download()
	print(f'\n Download Completed...:\n {ytv.title} \n {ytv_streams[strm_no]}')
