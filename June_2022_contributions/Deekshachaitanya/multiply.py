def multiplyEven(num1, num2, num3, num4):
    if(num1 % 2) != 0:
        num1 = 1
    if(num2 % 2) != 0:
        num2 = 1
    if(num3 % 2) != 0:
        num3 = 1
    if(num4 % 4) != 0:
        num4 = 1
    retVal = num1*num2*num3*num4
    return retVal
