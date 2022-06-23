import statistics
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print("The maximum number of the two numbers is",a)
    print("The minimum number of the two numbers is",b)
else:
    print("The maximum number of the two numbers is",b)
    print("The minimum number of the two numbers is",a)
l=[a,b]
c=statistics.mean(l)
print("The average of the two numbers is ",c)
d=sum(l)
print("The sum of two numbers is ",d)
f=a*b
print("The product of two numbers is",f)

