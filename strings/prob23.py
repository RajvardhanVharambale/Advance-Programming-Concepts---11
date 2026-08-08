string = input("Enter a string: ")

result = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count = count + 1
    else:
        result = result + string[i] + str(count)
        count = 1

if len(result) < len(string):
    print("Compressed string:", result)
else:
    print("Original string:", string)