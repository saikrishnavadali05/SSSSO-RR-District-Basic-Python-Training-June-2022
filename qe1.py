# Python program to perform Addition Subtraction Multiplication
# and Division of two numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)



#Enter First Number: 25
#Enter Second Number: 35
#Enter which operation would you like to perform?
#Enter any of these char for specific operation +,-,*,/: *
#25 * 35 : 875