sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count = count + 1

print("Occurrences of", word, ":", count)
