#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

number1 = 23
number2 = 24

#find max and min
if( number1 > number2):
    print(number1,"is maximun")
    print(number2,"is minimum")
else:
    print(number2,"is maximun")
    print(number1,"is minimum")

#average
print("The average of ", number1, "and", number2, "is:", ((number1+number2)//2))
print("The addition of ", number1, "and", number2, "is:", (number1+number2))
print("The Multiplication of ", number1, "and", number2, "is:", (number1 * number2))
