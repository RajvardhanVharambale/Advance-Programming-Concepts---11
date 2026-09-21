class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __gt__(self, s):
        return self.marks > s.marks
    def __lt__(self, s):
        return self.marks < s.marks
s1 = Student("Danny", 85)
s2 = Student("Aprilla", 75)
print("s1 > s2:", s1 > s2)
print("s1 < s2:", s1 < s2)