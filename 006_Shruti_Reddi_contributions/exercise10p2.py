#Write a function that take three integers and compare which the largest and smallest among the them. take input from the end user.

num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))
def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The largest of the 3 numbers is : ", largest_num)
def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    print("The smallest of the 3 numbers is : ", smallest_num)
largest(num1, num2, num3)
smallest(num1, num2, num3)
