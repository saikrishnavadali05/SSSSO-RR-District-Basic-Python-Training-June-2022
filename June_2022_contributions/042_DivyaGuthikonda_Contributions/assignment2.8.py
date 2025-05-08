#Write a program to check if the input string is a palindrome?
# Next, Make the program to work on integers as well. Write a palindrome function. 
# Call that function of 5 different inputs to test whether the function is written properly or not

n=str(input("Enter String: "))
def palindrome(n):
    return n == n[::-1]
a = palindrome(n)
if a:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

n1=str(input("Enter String: "))
b = palindrome(n1)
if b:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

n2=str(input("Enter String: "))
c = palindrome(n2)
if c:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

n3=str(input("Enter String: "))
d = palindrome(n3)
if d:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

n4=str(input("Enter String: "))
e = palindrome(n4)
if e:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

'''
Enter String: deined  
The given string is not a palindrome
Enter String: rotater
The given string is not a palindrome
Enter String: 16461
The given string is palindrome
Enter String: level
The given string is palindrome
Enter String: 21madam12 
The given string is palindrome
'''