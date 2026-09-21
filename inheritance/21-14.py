class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def make_call(self):
        print("Calling...")


class Smartphone(Camera, Phone):
    def use(self):
        self.take_photo()
        self.make_call()


s = Smartphone()
s.use()