# Write a script for factorial and take input from the command line parameter. using while and for loops

from sys import argv

Factorial_Number = int(argv[1])
Solution_Using_For_Loop = 1
Solution_Using_While_Loop = 1
n = 1
print("Using For loop")
for i in range(1,Factorial_Number+1):
    Solution_Using_For_Loop = i*Solution_Using_For_Loop
    i = i+1
print("The Factorial of the number is",Solution_Using_For_Loop)
print("Using While loop")
while (n < Factorial_Number+1):
    Solution_Using_While_Loop = n*Solution_Using_While_Loop
    n = n+1
print("The Factorial of the number is",Solution_Using_While_Loop)

# Write a script to print the count of number of digits within the given input number using while loop
Number1 = int(input("Enter the number "))
Number_of_digit = 0
while Number1 > 0:
    Number1 = Number1 // 10
    Number_of_digit = 1 + Number_of_digit
print("The number of Digits are",Number_of_digit)

