
string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in string:
    if ch in "AEIOUaeiou":
        vowels = vowels + 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        consonants = consonants + 1
    elif '0' <= ch <= '9':
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)