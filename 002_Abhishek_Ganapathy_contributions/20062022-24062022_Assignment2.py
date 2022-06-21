# Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

Number1 = int(input("Enter one number "))
Number2 = int(input("Enter second number "))
if(Number1 > 0 and Number2 > 0):
    if(Number1 > Number2):
        print("The Maximum of the 2 numbers are ", Number1)
        print("The Minimum of the 2 numbers are ", Number2)
    elif(Number2 > Number1):
        print("The Maximum of the 2 numbers are ", Number2)
        print("The Minimum of the 2 numbers are ", Number1)
    else:
        print("Both Numbers are same")
Addition =  Number1 + Number2        
Average = (Number1+Number2)/2
Multiplication = Number1*Number2
print("The Addition of 2 numbers are",Addition)
print("The Average of 2 numbers are",Average)
print("The multiplications of 2 numbers are",Multiplication)
