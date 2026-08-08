string = input("Enter a string: ")

for char in string:
    if string.index(char) == string.find(char):
        print(char, ":", string.count(char))