from pytube import YouTube

url = input("Enter YT Video URL: ")
ytv = YouTube(url)
print(f'\n Video Title: {ytv.title}')

ytv_streams = ytv.streams.all()
ytv_streams_li = list((enumerate(ytv_streams)))

print("\n Stream lists:")
for stream in ytv_streams_li:
    print(stream)
print()

strm_no = int(input("Enter stream no: "))

print(f' Downloading...:\n {ytv_streams[strm_no]} ')
ytv_streams[strm_no].download()
print(f'\n Download Completed...:\n {ytv.title} \n {ytv_streams[strm_no]}')
