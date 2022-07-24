# Write a script for multiplication of two numbers(int or float) and the input is taken from the user. When the user gives strings the error should be handled.
print("Question 1")

try:
    IntNumbers1 = int(input("Enter Whole number1 "))
    IntNumbers2 = int(input("Enter Whole number2 "))
    MultiplicationInt = IntNumbers1*IntNumbers2
    print("The Multiplication of",IntNumbers1,"and",IntNumbers2,"is",MultiplicationInt)
except:
    print("Please enter whole numbers only")

try:
    FloatNumbers1 = int(input("Enter Float number1 "))
    FloatNumbersz2 = int(input("Enter Float number2 "))
    MultiplicationFloat = FloatNumbers1*FloatNumbers2
    print("The Multiplication of",FloatNumbers1,"and",FloatNumbers2,"is",MultiplicationFloat)
except:
    print("Please enter Float numbers only")