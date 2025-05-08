def add(a,b,c,d):
    print("Addition of 4 numbers")
    return a+b+c+d;
def mul(a,b,c,d):
    print("Multiplication of 4 numbers")
    return a*b*c*d;
from files import Add
from files import Multi
def calculator():
    a=int(input("Enter number"))
    b=int(input("Enter number"))
    c=int(input("Enter number"))
    d=int(input("Enter number"))
    z=int(input("choose 1 for Addition or 2 for Multiplication"))
    for num in a,b,c,d:
        if num % 2 == 0:
            print(".")
            
        elif num % 2 !=0:
            print ("Odd number found...")
            print("Avoid Odd number to process")
            break
    if (z==1):
        print(Add.add(a,b,c,d))
    elif(z==2):
        print(Multi.mul(a,b,c,d))
    else:
        print("Choose only 1 or 2 only")
    
calculator()
