# Write a program to check common characters in two input strings.

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

str1 = set(str1)
str2 = set(str2)

common_chars = str1.intersection(str2)
print("The common characters are: ")

print(", ".join(common_chars))
