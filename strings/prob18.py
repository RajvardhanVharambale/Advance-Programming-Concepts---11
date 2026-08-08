string = input("Enter a string: ")

result = ""

for char in string:
    if char not in result:
        result = result + char

print("After removing duplicates:", result)