from YoutubeVideo import YoutubeVideo

def App():
    link = input("\nEnter the YouTube video URL: ")
    resolution = input("\nEnter the option: \n\nhighest resolution (1),\nlowest resolution (2)\n or \naudio only (3):\n\n")

    youtube_video = YoutubeVideo(link, App)
    youtube_video.download(resolution)

App()


# def Download(link, resolution):
#     youtubeObject = YouTube(link)

#     if resolution == 1:
#         youtubeObject = youtubeObject.streams.get_highest_resolution()
#     elif resolution == 2:
#         youtubeObject = youtubeObject.streams.get_lowest_resolution()
#     else:
#         print("Invalid resolution")
#         return

#     try:
#         youtubeObject.download("./videos/", youtubeObject.title+".mp4")
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")