class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


c = Car("Toyota", "Fortuner", "Diesel", 4000000)
c.display()
print("Discounted Price:", c.discounted_price(10))