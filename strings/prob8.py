#8. Frequency of a Character
string = input("Enter a string: ")
char = input("Enter the character to find: ")

count = 0

for ch in string:
    if ch == char:
        count = count + 1

print("Frequency =", count)