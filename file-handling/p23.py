file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:

    print("Both files are identical.")

else:

    print("Files are different.")

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):

        line1 = lines1[i].strip() if i < len(lines1) else ""
        line2 = lines2[i].strip() if i < len(lines2) else ""

        if line1 != line2:

            print("First difference found at line:", i + 1)
            print("File 1:", line1)
            print("File 2:", line2)

            break