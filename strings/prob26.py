message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for char in message:
    if char.isupper():
        encrypted = encrypted + chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        encrypted = encrypted + chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted = encrypted + char

print("Encrypted message:", encrypted)

decrypted = ""

for char in encrypted:
    if char.isupper():
        decrypted = decrypted + chr((ord(char) - 65 - shift) % 26 + 65)
    elif char.islower():
        decrypted = decrypted + chr((ord(char) - 97 - shift) % 26 + 97)
    else:
        decrypted = decrypted + char

print("Decrypted message:", decrypted)