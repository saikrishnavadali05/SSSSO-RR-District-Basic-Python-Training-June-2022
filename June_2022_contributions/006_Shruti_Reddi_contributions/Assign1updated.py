#Write a program to print the add, subtract, divide, multiply,
#  of the digits using functions. 
# Add, subtract, divide, multiply functions should be created.
#  For example, if the input is 235, the result should be 10.
#  Next, Load the input number 235 from a text file input.txt.
#  Next, Save the program output into a text file output.txt.

def addNumDig(n):
    sum = 0
    while n>0:
        rem = n%10
        sum = sum+rem
        n = int(n/10)
    return sum

print("Enter a Number: ", end="")
num = int(input())

res = addNumDig(num)
print("\nSum of Digits of " +str(num)+ " = " +str(res))

def subdigit(n):
    sub = 0
    while n>0:
        rem = n%10
        sub = sub-rem
        n = int(n/10)
    return sub

print("Enter a Number: ", end="")
num = int(input())

res = subdigit(num)
print("\nSub of Digits of " +str(num)+ " = " +str(res))

def multiplys(n):
    mul = 1
    while n>0:
        mult = n%10
        mul= mult*mul
        n = int(n/10)
    return mul

print("Enter a Number: ", end="")
num = int(input())

res = multiplys(num)
print("\nSub of Digits of " +str(num)+ " = " +str(res))
