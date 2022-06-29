def min_max(a,b,c):
    if(a>b) and (a>c):
        print(a,"is the largest")
    else:
        if(b>a) and (b>c):
            print(b, "is the largest")
        else:
            print(c,"is the largest")
    if(a<b) and (a<c):
        print(a,"is the smallest")
    else:
        if(b<a) and (b<c):
            print(b,"is the smallest")
        else:
            print(c,"is the smallest")                
n1=int(input("Enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
min_max(n1,n2,n3)                   