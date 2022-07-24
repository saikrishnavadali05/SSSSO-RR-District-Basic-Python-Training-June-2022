#Write a program to print the add, subtract, divide, multiply, of the digits using functions.
# Add, subtract, divide, multiply functions should be created.
# For example, if the input is 235, the result should be 10. 
# Next, Load the input number 235 from a text file input.txt. 
# Next, Save the program output into a text file output.txt.
file=open('input.txt','r')
data=file.read()
file.close()#here input is taken from input.txt file
h=open('input.txt','r')#142637
content=h.readlines()
def getSum(data):
    sum=0
    for digit in str(data):
        sum += int(digit)
    return sum
def getSub(data):
    sub=0
    for digit1 in str(data):
        sub -= int(digit1)
    return sub
def getMultiply(data):
    mul=1
    for digit2 in str(data):
        mul *= int(digit2)
    return mul
def getdiv(data):
    div=1
    for digit3 in str(data):
        div /= int(digit3)
    return div
f=open("output.txt","a")
print("The data that is storing in this text file is from assignment 2.1 :",file=f)
print("addition of digits of given number: ",getSum(data),file=f)
print("substraction of digits of given number: ",getSub(data),file=f)
print("Multiplication of digits of given number: ",getMultiply(data),file=f)
print("Division of digits of given number: ",getdiv(data),file=f)
f.close()
#Here the output is stored in output.txt file
'''output
The data that is storing in this text file is from assignment 2.1 :
addition of digits of given number:  23
substraction of digits of given number:  -23
Multiplication of digits of given number:  1008
Division of digits of given number:  0.000992063492063492
'''