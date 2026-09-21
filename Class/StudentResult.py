class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def total(self):
        return sum(self.marks)
    def percentage(self):
        return self.total() / 5
    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A"
        elif p >= 75:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "F"
    def display(self):
        print("Student Name:", self.name)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())
    def __del__(self):
        print("Student result object destroyed")
s = StudentResult("Sunny", [85, 90, 78, 88, 92])
s.display()
del s