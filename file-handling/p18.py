def display_employees(employees):
    print("\nAll Employees:")

    for emp in employees:
        print(emp[0], emp[1], emp[2], emp[3])


def highest_paid(employees):
    highest = max(employees, key=lambda x: x[3])

    print("\nHighest Paid Employee:")
    print("ID:", highest[0])
    print("Name:", highest[1])
    print("Department:", highest[2])
    print("Salary:", highest[3])


def average_salary(employees):
    total = 0

    for emp in employees:
        total += emp[3]

    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary, ":")

    for emp in employees:
        if emp[3] > salary:
            print(emp[0], emp[1], emp[2], emp[3])


file = open("employees.txt", "r")

employees = []

for line in file:
    data = line.strip().split(",")

    employee_id = data[0]
    name = data[1]
    department = data[2]
    salary = float(data[3])

    employees.append([employee_id, name, department, salary])

file.close()


display_employees(employees)

highest_paid(employees)

average_salary(employees)

salary = float(input("\nEnter salary: "))

above_salary(employees, salary)