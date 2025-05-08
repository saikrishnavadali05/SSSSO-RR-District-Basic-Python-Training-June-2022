from add import addEven
from multiply import multiplyEven

noofelements = 4
lis = []
for x in range(noofelements):
    lis.append(input("input:"))
if (len(lis)) < 4:
    raise Exception("Please Enter Four numbers")
num1 = int(lis[0])
num2 = int(lis[1])
num3 = int(lis[2])
num4 = int(lis[3])

if ((num1 % 2) != 0) and ((num2 % 2) != 0) and ((num3 % 2) != 0) and ((num4 % 2) != 0):
    raise Exception("No Number is Even number in given inputs")

sumof4 = addEven(num1, num2, num3, num4)
productof4 = multiplyEven(num1, num2, num3, num4)

outputfile = open("output.txt", "w")
lst = ["sum of even numbers:", str(sumof4), "\nproduct of even numbers:", str(productof4)]
outputfile.writelines(lst)
