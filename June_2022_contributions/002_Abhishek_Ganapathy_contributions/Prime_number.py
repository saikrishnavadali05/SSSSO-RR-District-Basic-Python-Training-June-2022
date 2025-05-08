Number1 = int(input("Please enter the number "))
Flag = False
if Number1 > 1:
    for i in range(2,Number1):
        if(Number1 % i) == 0:
            Flag = True
            break
if(Flag == True):
    print(Number1,"is not a prime number")
else:
    print(Number1,"is a prime number")

