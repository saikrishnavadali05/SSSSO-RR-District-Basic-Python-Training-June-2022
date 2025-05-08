#15.Write a function calculate() such that it can accept two variables and calculate the addition, multiplication of them. The result must be returned a single return call. The two variables are lists. (Do arithmetic operations on lists).
def Calculate(No1, No2):
    print("The sum is ",No1 + No2) 
    print("The multiplication is ",No1 * No2)
    if (No1 > No2):
        print("The Division is ",No1/No2)
        print("The Subtraction is ",No1 - No2)
    else:
        print("The Division is ",No2/No1)
        print("The Subtraction is ",No2 - No1)
    
Number1 = int(input("Enter your first number of your choice "))
Number2 = int(input("Enter your second number of your choice "))
Calculate(Number1,Number2)