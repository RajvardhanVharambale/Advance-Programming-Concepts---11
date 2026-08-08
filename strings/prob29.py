sentence = input("Enter a sentence: ")

words = sentence.split()

words.reverse()

result = " ".join(words)

print("Reversed sentence:", result)