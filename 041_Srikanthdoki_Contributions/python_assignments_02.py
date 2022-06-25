print("2. Write a program to find the maximum, minimum, \
average, addition, multiplication of any 2 integer numbers \
(for example : 23 and 34)")

a = int(input("Enter the a number: "))
b = int(input("Enter the b number: "))
print("Maximum number of given two numbers: ",a if a >= b else b)
print("Minimum number of given two numbers: ",a if a <= b else b)
print("Average of two numbers: ", (a + b) /2)
print("Addition of two numbers: ", a + b)
print("Multiplication of two numbers: ", a * b)
