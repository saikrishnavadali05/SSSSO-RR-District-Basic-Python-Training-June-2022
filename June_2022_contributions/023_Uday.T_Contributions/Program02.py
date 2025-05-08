#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

# printing the maximum value
maxVal = max(num1, num2)
print("The maximum  value for given two integer number  is", maxVal)
#printing the minimum value
minVal=min(num1,num2)
print("The minimum  value for given two integer number  is", minVal)
#printing the average value
avg=(num1+num2)/2
print("The average  value for given two integer number = %0.2f" %avg)
#printing the additionof two given value
sum=num1+num2
print("The addition  of given two integer number  is", sum)
#printing the multiplication of two given value
mul=num1*num2
print("The multiplication of given two integer number is",mul)2