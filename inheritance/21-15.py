class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name)
        print(self.age)
        print(self.roll_no)
        print(self.course)
        print(self.topic)
        print(self.guide)


r = ResearchStudent("Parth", 20, 10, "CSE", "AI", "Dr. Patil")
r.display()