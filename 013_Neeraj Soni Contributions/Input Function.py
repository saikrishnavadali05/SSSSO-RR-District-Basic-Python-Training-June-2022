name_of_the_student = input("write the name of the student -")
print("name of the student is", name_of_the_student)
print(type(name_of_the_student))
print("--------------------------")
First_Number = input("Write the first number -")
print("the first number is -", First_Number)
print(type(First_Number))
FFirst_Number = int(First_Number)
print(type(FFirst_Number))
print("-----------")
from sys import argv
num1 = argv[1]
num2 = argv[2]
num3 = int(argv[3])
num4 = int(argv[4])
addition1 = num1 + num2
addition2 = num3 + num4
print("The total addition1 result is", addition1)
print("The total addition2 result is", addition2)