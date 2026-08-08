string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

string1 = string1.lower()
string2 = string2.lower()

if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")