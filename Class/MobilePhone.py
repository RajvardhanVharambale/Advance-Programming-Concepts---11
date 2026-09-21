class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)
    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)
m = MobilePhone("Samsung", "S25", "256GB", 70000)
m.display()
print("Price after 10% discount:", m.discount_price(10))