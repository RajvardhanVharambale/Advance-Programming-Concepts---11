class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", self.marks + self.points)


s = Student(85, 15)
s.performance()