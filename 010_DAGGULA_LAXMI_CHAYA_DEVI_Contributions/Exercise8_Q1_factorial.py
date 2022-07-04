#finding factorial of a number

from math import factorial
from sys import argv
number=int(argv[1])
Num=number
Num2=number

if number<0:
    print("Factorial does not exist")
elif number==0:
    print("Factorial is 1")
else:
#using while loop
    fact=1
    while number>0:
        fact*=number
        number=number-1
    print("Factorial of {0} is {1}".format(Num2,fact))

#using for loop
    fac=1
    for i in range(1,Num):
        fac*=i
    fac*=Num
    print("factorial of {0} is {1}".format(Num2,fac))
