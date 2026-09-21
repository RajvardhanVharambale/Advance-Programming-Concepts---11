class Employee:
    def calculate_salary(self):
        print("Employee Salary")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary: 80000")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: 60000")
class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary: 50000")
employees = [Manager(), Developer(), Tester()]
for e in employees:
    e.calculate_salary()