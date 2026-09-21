class Vehicle:
    def __init__(self, vehicle_no, model, rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rate = rate
        self.availability = availability
    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle Rented")
        else:
            print("Vehicle Not Available")
    def return_vehicle(self):
        self.availability = True
        print("Vehicle Returned")
    def rental_charges(self, days):
        return self.rate * days
    def display(self):
        print("Vehicle No:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rate)
        print("Available:", self.availability)
v = Vehicle("MH09AB1234", "Swift", 1000, True)
v.display()
v.rent()
print("Rental Charges:", v.rental_charges(3))
v.return_vehicle()
v.display()