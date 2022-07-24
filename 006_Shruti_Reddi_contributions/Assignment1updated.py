#Write a program to print the add, subtract, divide, multiply,
#  of the digits using functions. 
# Add, subtract, divide, multiply functions should be created.
#  For example, if the input is 235, the result should be 10.
#  Next, Load the input number 235 from a text file input.txt.
#  Next, Save the program output into a text file output.txt.
num = int(input())
def addNumDig(xyz):
    sum = 0
while num>0:
    rem = num%10
    sum = sum+rem
    num = int(num/10)

print("Enter a Number: ", end="")
num = int(input())

res = addNumDig(num)
print("The addition of digits is : ", res)


