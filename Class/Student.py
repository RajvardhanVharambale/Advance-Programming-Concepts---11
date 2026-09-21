class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def percentage(self):
        return sum(self.marks) / len(self.marks)
    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
s1 = Student(1, "Jerry", [80, 85, 90])
s2 = Student(2, "Tom", [75, 80, 85])
s1.display()
print()
s2.display()