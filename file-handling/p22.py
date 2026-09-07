file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()

file3 = open("file3.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file3.close()

print("Both files merged successfully into file3.txt")