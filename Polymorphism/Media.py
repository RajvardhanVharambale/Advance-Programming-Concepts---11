class Media:
    def play(self):
        print("Playing Media")
class Audio(Media):
    def play(self):
        print("Playing Audio")
class Video(Media):
    def play(self):
        print("Playing Video")
class Podcast(Media):
    def play(self):
        print("Playing Podcast")
media = [Audio(), Video(), Podcast()]
for m in media:
    m.play()