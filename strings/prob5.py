
string = input("Enter a string: ")
upper = 0
lower = 0

for ch in string:
    if 'A' <= ch <= 'Z':
        upper = upper + 1
    elif 'a' <= ch <= 'z':
        lower = lower + 1

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)