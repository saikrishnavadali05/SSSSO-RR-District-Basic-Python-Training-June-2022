"""
Write a program to print the add, subtract, divide, multiply, 
of the digits using functions. 
Add, subtract, divide, multiply functions should be created. 
For example, if the input is 235, the result should be 10. 
Next, Load the input number 235 from a text file input.txt. 
Next, Save the program output into a text file output.txt.
"""

from re import sub


def add(num):
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem
        num //=10
    return sum

def subtract(num):
    sub = 0
    while num > 0:
        rem = num % 10
        sub -= rem
        num //= 10
    return sub

def divide(num):
    divide = 1
    while num > 0:
        rem = num % 10 
        divide /= rem
        num //= 10
    return divide

def multiply(num):
    mul = 1
    while num > 0:
        rem = num % 10
        mul *= rem
        num //= 10
    return mul 

f = open("input.txt",'r')
f1 = open("output.txt","w")
x = f.readline()
p = add(int(x))
q = subtract(int(x))
r = divide((int(x)))
s = multiply(int(x))
f1.write("The addition of given numbers of input text is:---"+str(p))
f1.write("\n")
f1.write("The subtraction of given nubmers of input text is:---"+str(q))
f1.write("\n")
f1.writelines("The Division of given numbers of input text is:---"+str(r))
f1.write("\n")
f1.writelines("The Multiplication of given numbers of input text is:---"+str(s))
f1.close()
f.close()