def AddEvenNumbers(num1, num2, num3, num4):
    if(num1 % 2) != 0:
        num1 = 0
    if(num2 % 2) != 0:
        num2 = 0
    if(num3 % 2) != 0:
        num3 = 0
    if(num4 % 4) != 0:
        num4 = 0
    sum = num1+num2+num3+num4
    return sum
