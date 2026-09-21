class Person:
    def display_role(self):
        print("Person")
class Student(Person):
    def display_role(self):
        print("Student")
class Faculty(Person):
    def display_role(self):
        print("Faculty")
class Administrator(Person):
    def display_role(self):
        print("Administrator")
people = [Student(), Faculty(), Administrator()]
for p in people:
    p.display_role()