file = open("student.txt", "r")

lines = file.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())

file.close()