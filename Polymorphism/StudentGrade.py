class Student:
    def calculate_grade(self, marks):
        print("Student Grade")
class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            print("Engineering Grade: A")
        else:
            print("Engineering Grade: B")
class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            print("Medical Grade: A")
        else:
            print("Medical Grade: B")
class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            print("Management Grade: A")
        else:
            print("Management Grade: B")
EngineeringStudent().calculate_grade(80)
MedicalStudent().calculate_grade(85)
ManagementStudent().calculate_grade(75)