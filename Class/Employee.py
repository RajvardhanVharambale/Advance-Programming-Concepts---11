class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    def hra(self):
        return self.basic_salary * 0.20
    def da(self):
        return self.basic_salary * 0.10
    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra())
        print("DA:", self.da())
        print("Gross Salary:", self.gross_salary())
e = Employee(101, "Micky", 30000)
e.display()