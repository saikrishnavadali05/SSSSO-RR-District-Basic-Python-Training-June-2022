from Assignment1_24_07_2022_add import add
from Assignment1_24_07_2022_Multiply import Multiply
Number1 = list(input("Enter the numbers "))
# Number_of_digit = 0
Digits = 0
Even = []
Length = len(Number1)
# while Number1 > 0:
#     Number1 = Number1 // 10
#     Number_of_digit = 1 + Number_of_digit
# print("The number of Digits are",Number_of_digit)
# Numberlist = list(Number1)
print("The number of Digits are",len(Number1))
# if Number_of_digit == 4:
if len(Number1) == 4:
    for i in range(0,len(Number1)):
        if(int(Number1[i]) % 2 == 0):
            Digits = Digits + 1
            Add = Number1[i]
            Even.append(Add)
            print("The Even Numbers are", Even)
        else:
            print("No Even Numbers found")
    else:
        print("Enter four numbers")

    add(Digits,Even)
    Multiply(Digits,Even)

