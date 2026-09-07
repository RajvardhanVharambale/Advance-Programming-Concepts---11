

class Student:
    def __init__(self, name):
        print(f"Constructor: {name} created")
        self.name = name

    def __del__(self):
        print(f"Destructor: {self.name} is being destroyed")

obj = Student("Raj's")
del obj