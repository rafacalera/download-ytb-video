
from pytube import YouTube

class YoutubeVideo:
    def __init__(self, link, app):
        self.link = link
        self.app = app
        self.set_youtube_link(link)

    def set_youtube_link(self, link):
        try:
            self.youtube_object = YouTube(link)
        except Exception as error:
            self.error(error)

    def filtrar_caracteres_especiais(self, string):
        caracteres_proibidos = r'<>:"/\|?*'
        resultado = ''.join(caracter for caracter in string if caracter not in caracteres_proibidos)
        return resultado

    def download(self, option):
        try:
            match option:
                case "1":
                    self.youtube_object = self.youtube_object.streams.get_highest_resolution()
                case "2":
                    self.youtube_object = self.youtube_object.streams.get_lowest_resolution()
                case "3":
                    self.youtube_object = self.youtube_object.streams.get_audio_only()

            filename = self.filtrar_caracteres_especiais(self.youtube_object.title) + ".mp4"
            if option == "3":
                filename = self.filtrar_caracteres_especiais(self.youtube_object.title) + ".mp3"

            self.youtube_object.download("./videos", filename)
            print("\nDownload is completed successfully")
            
            other_video = input("\nDo you want to download another video? (y/n): ")
        
            if other_video == "y":
                return self.app()
            else:
                return
        except Exception as error:
            self.error(error)
        
    def error(self, error):
        print("\nAn error has occurred:\n", error, "\n")
        return self.app()