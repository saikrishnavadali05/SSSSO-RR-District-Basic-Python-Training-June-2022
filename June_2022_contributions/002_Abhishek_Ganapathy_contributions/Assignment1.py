# Write a program to print the sum of the digits. For example if the input is 123, the result should be 6.
Number = int(input("Enter the number "))
Sum = 0
while (Number > 0):
    Remainder = Number%10
    Sum = Sum + Remainder
    Number = Number//10
    print("Remainder",Remainder)
    print("Sum",Sum)
    print("Number",Number)
print("Sum of the digits", Sum)


