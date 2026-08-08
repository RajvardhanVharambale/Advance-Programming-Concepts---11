password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")