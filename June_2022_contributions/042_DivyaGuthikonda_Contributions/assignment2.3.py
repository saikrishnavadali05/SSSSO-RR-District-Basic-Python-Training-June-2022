#Write a program that accepts a positive integer n. Next, write a function to find factorial of the number.
#  and next, write another function to compute the value of n+nn+nnn.
#  If n is 5, first output should be 5! = 120 and the next output should be 5+55+555 = 615.
n=int(input("Enter Number: "))
def fact(n):
    return 1 if(n==1 or n==0) else n* fact(n-1)
def sum(n):
    b=n+(n*10+n)+(n*100+n*10+n)
    return b

print("Factorial of",n,"!","is:", fact(n))
print("Answer of",n,"+",n,n,"+",n,n,n,"is",sum(n))

#output
#Enter Number: 5
#Factorial of 5 ! is: 120
#Answer of 5 + 5 5 + 5 5 5 is 615
