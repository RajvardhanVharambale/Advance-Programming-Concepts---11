n = int(input("Enter number: "))

i = 2
prime = True

while i < n:
    if n % i == 0:
        prime = False
        break
    i += 1

if n <= 1:
    print("Not Prime")
elif prime:
    print("Prime")
else:
    print("Not Prime")