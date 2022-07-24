num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter thrid Number: "))
num4 = int(input("Enter fourth Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,*: ")

result = 0
if ch == '+':
    result = num1 + num2 + num3 + num4
elif ch == '*':
    result = num1 * num2 * num3 * num4
else:
    print("Input character is not recognized!")
print(num1, ch , num2, ":", result)
