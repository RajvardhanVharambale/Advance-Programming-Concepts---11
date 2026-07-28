import math

num = int(input("Enter number: "))

root = int(math.sqrt(num))

count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count += 1

if count == 2:
    print(root, "is Prime")
else:
    print(root, "is Not Prime")