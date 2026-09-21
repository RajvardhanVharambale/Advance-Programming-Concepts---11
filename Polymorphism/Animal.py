class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog: Bark")
class Cat(Animal):
    def sound(self):
        print("Cat: Meow")
class Cow(Animal):
    def sound(self):
        print("Cow: Moo")
class Lion(Animal):
    def sound(self):
        print("Lion: Roar")
animals = [Dog(), Cat(), Cow(), Lion()]
for a in animals:
    a.sound()