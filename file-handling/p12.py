file = open("student.txt", "r")

content = file.read().lower()

words = content.split()

word_count = {}

for word in words:
    word = word.strip(".,!?;:")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()