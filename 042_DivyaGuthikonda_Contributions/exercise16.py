#Write a script for multiplication of two numbers(int or float) and the input is taken from the user. When the user gives strings the error should be handled
from sys import argv
try:
    a=int(input("Give first number: "))
    b=float(input("Give first number: "))
    multiply=a*b
    print(multiply)
except:
    print("Error: Provide two numbers.")
    