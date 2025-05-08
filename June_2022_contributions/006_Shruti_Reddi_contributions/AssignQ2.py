#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

num1=23
num2=34

#defining Maximum and minimum using formula

maximum=((num1+num2+abs(num1-num2))//2)
print('The maximum of 23 and 34 is =', maximum)

minimum=((num1+num2-abs(num1-num2))//2)
print('The minimum of 23 and 34 is =', minimum)

#defining average of the given numbers
average=(num1+num2)/2
print('The average of 23 and 34 is =', average)

#defining addition and multiplication of the given numbers

addition= num1+num2
print('The addition of 23 and 34 is =', addition)

multiplication=num1*num2
print('The multiplication of 23 and 34 is =', multiplication)