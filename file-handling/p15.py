file = open("program.py", "r")

lines = file.readlines()

file.close()

output = open("program_without_comments.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        output.write(line)

output.close()

print("Comments removed successfully.")