'''
2.	Write a program to find the maximum, minimum, average,
addition, multiplication of any 2 integer numbers
(for example : 23 and 34)

'''  
Num1 = int(input("Enter Num1 integer value:"))
Num2 = int(input("Enter Num2 integer value:"))

# calculate average of given numbers
avg = (Num1 + Num2) / 2

print("Maximum value of", Num1, "and", Num2, "is:", max(Num1, Num2))
print("Minimum value of", Num1, "and", Num2, "is:", min(Num1, Num2))
print("The average of", Num1, "and", Num2, "is:", "%0.2f" %avg)
print("Sum of", Num1, "and", Num2, "is:", (Num1+Num2))
print("Multiplication of", Num1, "and", Num2, "is:", (Num1*Num2))