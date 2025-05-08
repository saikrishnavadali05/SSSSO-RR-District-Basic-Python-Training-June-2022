"""
Write a script to check whether the given number is odd or even by 
requesting input from the user, using input() function.
"""
num = int(input("Enter the integer number: "))

if num % 2 == 0:
    print("Given number is an even")
else:
    print("Given number is an odd")