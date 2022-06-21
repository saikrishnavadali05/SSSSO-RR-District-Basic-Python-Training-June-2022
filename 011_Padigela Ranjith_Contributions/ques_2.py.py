# 2. Write a program to find the maximum, minimum, average, addition, multiplication 
# of any 2 integer numbers (for example : 23 and 34)

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the another number: "))

if num1 > num2:
    print('maximum of number is: ',num1)
else:
    print('maximum of number is: ',num2)


if num1 < num2:
    print('minimum of number is: ',num1)
else:
    print('minimum of number is: ',num2)

print('The average of the given numbers is: ',(num1 + num2)/2)

print('The addition of the given numbers is: ',num1 + num2)

print('The multiplication of the given numers is: ',num1 * num2)