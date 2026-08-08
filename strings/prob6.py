#6. Replace Characters
string = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in string:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("Updated String =", result)
