string = input("Enter a string: ")

most_frequent = string[0]
max_count = 0

for char in string:
    count = string.count(char)

    if count > max_count:
        max_count = count
        most_frequent = char

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)