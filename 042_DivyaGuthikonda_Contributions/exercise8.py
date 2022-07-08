#Write a script for factorial and take input from the command line parameter. using while and for loops
# With While loop
def factorial(n):
    number=1
    while n>= 1:
        number=number*n
        n=n-1
    return number
a=int(input("Enter Number : "))
f=factorial(a)
print("The factorial of given number is :", f)
#Enter Number : 10
#The factorial of given number is : 3628800

#with For loop
def factorial(n):
    number=1
    for i in range(n):
        number=number*(i+1)
    return number
a=int(input("Enter Number :"))
f=factorial(a)
print("Factorial of Given Number is :", f)
#Enter Number :5
#Factorial of Given Number is : 120

#Write a script to print the count of number of digits within the given input number using while loop

