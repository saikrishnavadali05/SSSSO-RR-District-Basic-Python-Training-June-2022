#Question2: Write a program to find the maximum, minimum, average, 
# addition, multiplication of any 2 integer numbers 
# (for example : 23 and 34)
Num1 = input("Enter integer value1:")
#print(type(Num1))
Num1 = int(Num1)
Num2 = input("Enter integer value2:")
#print(type(Num2))
Num2 = int(Num2)
if Num1>Num2:
    print("Num1 is Maximun")
    print("Num2 is minimum")
elif Num2>Num1:
    print("Num2 is Maximun")
    print("Num1 is minimum")
else:
    print("Num1 equals to Num1")

print("Average of two numbers =",(Num1+Num2)/2)
Addition=Num1+Num2
print("Addition of two numbers =" , Addition)
Multiplication=0
for i in range(Num2):
    Multiplication+=Num1
print("Multiplication of two numbers =" , Multiplication)
