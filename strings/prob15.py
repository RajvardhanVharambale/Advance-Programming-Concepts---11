string = input("Enter a string: ")

duplicates = ""

for char in string:
    if string.count(char) > 1 and char not in duplicates:
        duplicates = duplicates + char

print("Duplicate characters:", duplicates)