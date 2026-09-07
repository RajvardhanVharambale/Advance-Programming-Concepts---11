file = open("students.txt", "r")

lines = file.readlines()

file.close()

students = []

for line in lines[1:]:
    data = line.strip().split(",")

    roll_no = data[0]
    name = data[1]
    marks = int(data[2])

    students.append([roll_no, name, marks])


# Display all records
print("All Student Records:")

for student in students:
    print(student[0], student[1], student[2])


# Highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print("Roll No:", highest[0])
print("Name:", highest[1])
print("Marks:", highest[2])


# Average marks
total = 0

for student in students:
    total += student[2]

average = total / len(students)

print("\nAverage Marks:", average)


# Students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student[0], student[1], student[2])