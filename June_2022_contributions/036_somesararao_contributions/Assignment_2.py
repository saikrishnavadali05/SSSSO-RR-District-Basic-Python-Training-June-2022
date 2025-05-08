# Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

Number1 = int(input("Enter one number "))
Number2 = int(input("Enter second number "))
if(Number1 > 0 and Number2 > 0):
    if(Number1 > Number2):
        print("The Maximum number is", Number1)
        print("The Minimum number is", Number2)
    elif(Number2 > Number1):
        print("The Maximum number is ", Number2)
        print("The Minimum number is ", Number1)
    else:
        print("Both Numbers are same")
Average = (Number1+Number2)/2
Addition =  Number1 + Number2        
Multiplication = Number1*Number2
print("The Average of 2 numbers are",Average)
print("The Addition of 2 numbers are",Addition)
print("The multiplications of 2 numbers are",Multiplication)