from add import *
from multiple import *

input_num1 = int(input("Enter first number: "))
input_num2 = int(input("Enter second number: "))
input_num3 = int(input("Enter third number: "))
input_num4 = int(input("Enter fourth number: "))
total_add = add_Number(input_num1,input_num2,input_num3,input_num4)
total_mul = multi_Number(input_num1,input_num2,input_num3,input_num4)
print("Sum of total even numbers is : " + str(total_add))
print("Multiplication of total even numbers is : " + str(total_mul))