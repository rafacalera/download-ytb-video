
from pytube import YouTube

class YoutubeVideo:
    def __init__(self, link, app):
        self.link = link
        self.app = app
        self.set_youtube_link(link)

    def set_youtube_link(self, link):
        try:
            self.youtubeObject = YouTube(link)
        except:
            self.error()


    def download(self, option):
        if option == "1":
            self.youtubeObject = self.youtubeObject.streams.get_highest_resolution()
        elif option == "2":
            self.youtubeObject = self.youtubeObject.streams.get_lowest_resolution()
        elif option == "3":
            self.youtubeObject = self.youtubeObject.streams.get_audio_only()
        else:
            print("\nInvalid Option")
            return self.app()

        try:
            self.youtubeObject.download("./videos/", self.youtubeObject.title+".mp4")
            print("\nDownload is completed successfully")
            
            other_video = input("\nDo you want to download another video? (y/n): ")
        
            if other_video == "y":
                return self.app()
            else:
                return
        except:
            self.error()
        
    def error(self):
        print("\nAn error has occurred")
        return self.app()