a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if(a>b):
    if(c>a):
        print(c, "is big")
    else:
        print(a, "is big")
else:
    if(c>b):
        print(c, "is big")
    else:
        print(b,"is big")
