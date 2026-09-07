file = open("student.txt", "r")

search_word = input("Enter word to search: ")

count = 0
line_numbers = []

line_no = 0

for line in file:
    line_no += 1

    words = line.split()

    for word in words:
        word = word.strip(".,!?;:")

        if word.lower() == search_word.lower():
            count += 1

            if line_no not in line_numbers:
                line_numbers.append(line_no)

print("Number of occurrences:", count)

if count > 0:
    print("Word found on line(s):", line_numbers)
else:
    print("Word not found.")

file.close()