file = open("student.txt", "r")

content = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

modified_content = content.replace(old_word, new_word)

file.close()

file = open("student_new.txt", "w")

file.write(modified_content)

file.close()

print("Word replaced successfully.")
print("Modified content saved in student_new.txt")