import math

class Shape:
    def display(self):
        print("Shape")


class Circle(Shape):
    def area(self, r):
        print("Circle Area:", math.pi * r * r)


class Rectangle(Shape):
    def area(self, l, b):
        print("Rectangle Area:", l * b)


class Triangle(Shape):
    def area(self, b, h):
        print("Triangle Area:", 0.5 * b * h)


c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(10, 5)

t = Triangle()
t.display()
t.area(10, 6)