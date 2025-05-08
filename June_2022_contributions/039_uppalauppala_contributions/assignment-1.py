Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

Ans:

1)   To find maximum of two numbers:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# printing the maximum value
if(num1 > num2):
  print(num1, "is greater")
elif(num1 < num2):
    print(num2, "is greater")
else:
    print("Both are equal")

2) To find minimum of two members:

numbers = [9, 34, 11, -4, 27]

# find the smallest number
min_number = min(numbers)
print(min_number)

3)To find average of two numbers:

# First Number
a = 5

# Second Number
b = 10

# Calculating average of two numbers
avg = (a + b) / 2

# Display output
print("Average of two numbers = %.2f" %avg)

4)To find multiplication of two integer numbers

num1=int(input("Enter the first number: "))
#input value for variable num1
num2=int(input("Enter the second number: "))
#input value for variable num2
mul=num1*num2;
#perform multiplication operation
print("the product of given numbers is: ",mul)
#display the product
