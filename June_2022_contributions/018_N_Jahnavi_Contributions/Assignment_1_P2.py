# program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

from statistics import mean


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# Operations

Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1/num2
Maximum = max(num1, num2)
Minimum = min(num1, num2)
Average = (num1 +num2)/2

print("Addition = ", Addition)
print("Subtraction = ", Subtraction)
print("Multiplication = ", Multiplication)
print("Division = ", Division)
print("Maximum = ", Maximum)
print("Minimum = ", Minimum)
print("Average = ", Average)




