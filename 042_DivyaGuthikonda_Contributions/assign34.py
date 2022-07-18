data=56
tot=0
while(data>0):
        dig=data%10
        tot=tot+dig
        data=data//10
print(tot)


def getSub(data):
    print("substraction of digits of given number: ")
    sub=0
    for digit1 in str(data):
        sub -= int(digit1)
    print(sub)
def getMultiply(data):
    print("Multiplication of digits of given number: ")
    mul=1
    for digit2 in str(data):
        mul *= int(digit2)
    print(mul)
def getdiv(data):
    print("division of digits of given number: ")
    div=1
    for digit3 in str(data):
        div /= int(digit3)
    print(div)
getSum(data)
getSub(data)
getMultiply(data)
getdiv(data)