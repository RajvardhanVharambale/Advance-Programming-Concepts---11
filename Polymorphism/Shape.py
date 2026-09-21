class Shape:
    def area(self):
        print("Area of shape")
class Circle(Shape):
    def area(self):
        print("Circle Area:", 3.14 * 5 * 5)
class Rectangle(Shape):
    def area(self):
        print("Rectangle Area:", 10 * 5)
class Triangle(Shape):
    def area(self):
        print("Triangle Area:", 0.5 * 10 * 5)
shapes = [Circle(), Rectangle(), Triangle()]
for s in shapes:
    s.area()