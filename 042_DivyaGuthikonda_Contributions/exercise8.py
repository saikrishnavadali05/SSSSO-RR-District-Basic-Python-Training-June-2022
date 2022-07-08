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
n=int(input("Enter Number : "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The Number of digits in the given number are :", count)
#Enter Number : 25896
#The Number of digits in the given number are : 5

