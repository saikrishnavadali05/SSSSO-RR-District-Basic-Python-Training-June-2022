from add import sum1
from multiply import multiply

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

sum = sum1(num1, num2, num3, num4)
product = multiply(num1, num2, num3, num4)

file1 = open("finaloutput.txt", "w")
lst = ["sum:", str(sum), "\nproduct:", str(product)]
file1.writelines(lst)
