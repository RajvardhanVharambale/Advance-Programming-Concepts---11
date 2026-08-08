string = input("Enter a string: ")

frequency = {}

for char in string:
    frequency[char] = string.count(char)

values = sorted(set(frequency.values()), reverse=True)

if len(values) < 2:
    print("Second most frequent character does not exist.")
else:
    second = values[1]

    for char in frequency:
        if frequency[char] == second:
            print("Second most frequent character:", char)
            print("Frequency:", second)
            break
        