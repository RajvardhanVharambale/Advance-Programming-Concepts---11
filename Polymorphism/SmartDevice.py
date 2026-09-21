class SmartDevice:
    def turn_on(self):
        print("Device ON")
    def turn_off(self):
        print("Device OFF")
class Light(SmartDevice):
    def turn_on(self):
        print("Light ON")
    def turn_off(self):
        print("Light OFF")
class Fan(SmartDevice):
    def turn_on(self):
        print("Fan ON")
    def turn_off(self):
        print("Fan OFF")
class AC(SmartDevice):
    def turn_on(self):
        print("AC ON")
    def turn_off(self):
        print("AC OFF")
class TV(SmartDevice):
    def turn_on(self):
        print("TV ON")
    def turn_off(self):
        print("TV OFF")
devices = [Light(), Fan(), AC(), TV()]
for d in devices:
    d.turn_on()
    d.turn_off()