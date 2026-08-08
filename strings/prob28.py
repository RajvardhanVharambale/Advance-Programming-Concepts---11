paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word Frequency:")

for word in frequency:
    print(word, ":", frequency[word])