"""
Write a program to check if the input string is a palindrome? 
Next, Make the program to work on integers as well. Write a palindrome function. 
Call that function of 5 different inputs to test whether 
the function is written properly or not.
"""

def Palindrome(string):
    temp = string
    rev = ""
    for i in string:
        rev = i + rev
    if temp==rev:
        return "Palindrome"
    else:
        return "Not a palindrome"

print(Palindrome("madam"))
print(Palindrome("12321"))
print(Palindrome("malayalam"))
print(Palindrome("HaraH"))
print(Palindrome("MissiM"))
