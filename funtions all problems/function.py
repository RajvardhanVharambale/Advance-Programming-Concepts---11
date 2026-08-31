# 1. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial:", factorial(n))


# 2. Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))


# 3. Greater of two numbers
def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater:", greater(a, b))


# 4. Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))


# 5. Prime Number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter number: "))

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")


# 6. Area of Circle
def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area:", area_circle(r))


# 7. Sum of first n natural numbers
def natural_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))
print("Sum:", natural_sum(n))


# 8. Power of a number
def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Answer:", power(base, exponent))


# 9. Largest element without max()
def largest(numbers):
    big = numbers[0]

    for i in numbers:
        if i > big:
            big = i

    return big

numbers = [10, 40, 20, 50, 30]
print("Largest:", largest(numbers))


# 10. Count vowels
def count_vowels(text):
    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

text = input("Enter string: ")
print("Vowels:", count_vowels(text))


# 11. Reverse a string
def reverse_string(text):
    return text[::-1]

text = input("Enter string: ")
print("Reverse:", reverse_string(text))


# 12. Palindrome
def palindrome(text):
    text = str(text)

    if text == text[::-1]:
        return True
    else:
        return False

text = input("Enter string or number: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


# 13. Average of list
def average(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]
print("Average:", average(numbers))


# 14. Count occurrence of an element
def count_element(numbers, element):
    count = 0

    for i in numbers:
        if i == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10]
element = int(input("Enter element: "))

print("Count:", count_element(numbers, element))


# 15. Unique elements
def unique_list(numbers):
    result = []

    for i in numbers:
        if i not in result:
            result.append(i)

    return result

numbers = [10, 20, 10, 30, 20, 40]
print("Unique list:", unique_list(numbers))


# 16. Second largest number
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

numbers = [10, 40, 20, 50, 30]
print("Second largest:", second_largest(numbers))


# 17. Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        c = a + b
        a = b
        b = c

    return result

n = int(input("Enter number of terms: "))
print("Fibonacci:", fibonacci(n))


# 18. Percentage and grade
def percentage_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = percentage_grade(marks[0], marks[1], marks[2], marks[3], marks[4])

print("Percentage:", percentage)
print("Grade:", grade)

# 19. Electricity bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units: "))
print("Bill:", electricity_bill(units))


# 20. Gross salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross salary:", gross_salary(basic))


# 21. Total bill after discount
def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount = total * 0.10
    final_bill = total - discount

    return final_bill

prices = [100, 200, 300]
quantities = [2, 1, 2]

print("Final bill:", total_bill(prices, quantities))


# 22. Minimum, maximum, sum and average
def calculate(numbers):
    small = numbers[0]
    big = numbers[0]
    total = 0

    for i in numbers:
        if i < small:
            small = i

        if i > big:
            big = i

        total = total + i

    average = total / len(numbers)

    return small, big, total, average

numbers = [10, 20, 30, 40, 50]

small, big, total, average = calculate(numbers)

print("Minimum:", small)
print("Maximum:", big)
print("Sum:", total)
print("Average:", average)