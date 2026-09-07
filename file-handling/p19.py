file = open("attendance.txt", "r")

print("Students with attendance below 75%:")

for line in file:

    data = line.strip().split(",")

    roll_no = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%")

file.close()