#factorial of the number using for and while loop
from re import I


n=int(input("Enter the number"))
#print("The given number is",n)
i=n
fact = 1
while i!=0:
    fact=fact*i
    i=i-1
print("The factorial of the number using while loop is",fact)
fact = 1
for i in range(1,n+1):
    fact=fact*i
print("The factorial of the number using for loop is ",fact)    




