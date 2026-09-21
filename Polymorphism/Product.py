class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, p):
        return self.price == p.price
    def __gt__(self, p):
        return self.price > p.price
p1 = Product("Mobile", 30000)
p2 = Product("Laptop", 30000)
print("Equal:", p1 == p2)
print("p1 is greater:", p1 > p2)