class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, engine):
        super().__init__(brand)
        self.engine = engine


class SportsCar(Car):
    def speed(self):
        print("Sports Car has high speed")


class ElectricBike(Bike):
    def range(self):
        print("Electric Bike has long battery range")


s = SportsCar("BMW", 2)
print("Brand:", s.brand)
print("Seats:", s.seats)
s.speed()

e = ElectricBike("Ather", "Electric")
print("Brand:", e.brand)
print("Engine:", e.engine)
e.range()