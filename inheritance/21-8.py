class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + 20000


class Developer(Employee):
    def salary(self):
        return self.basic_salary + 15000


class Tester(Employee):
    def salary(self):
        return self.basic_salary + 10000


m = Manager(101, "Amit", 50000)
d = Developer(102, "Rahul", 40000)
t = Tester(103, "Sneha", 35000)

print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())