class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units
    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 2
        elif self.units <= 200:
            return 100 * 2 + (self.units - 100) * 3
        else:
            return 100 * 2 + 100 * 3 + (self.units - 200) * 5
    def display(self):
        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Electricity Bill:", self.calculate_bill())
e = ElectricityBill(101, "Minnie", 250)
e.display()