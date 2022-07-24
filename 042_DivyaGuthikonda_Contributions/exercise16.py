#Write a script for multiplication of two numbers(int or float) and the input is taken from the user. When the user gives strings the error should be handled
from sys import argv
try:
    a=int(input("Give first number: "))
    b=float(input("Give first number: "))
    multiply=a*b
    print(multiply)
except:
    print("Error: Provide two numbers.")

#(two inputs are integers)
#  Give first number: 12
#  Give first number: 15
#  180.0

#(one input is integer and other is a float)
#Give first number: 26
#Give first number: 25.256
#656.656

#(if we enter any strinng)
#Give first number: hi
#Error: Provide two numbers.