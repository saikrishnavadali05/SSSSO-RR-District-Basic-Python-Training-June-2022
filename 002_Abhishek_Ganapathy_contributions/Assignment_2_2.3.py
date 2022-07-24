def Sum(Number):
        Sum_of_Number = Number + Number*Number + Number*Number*Number
        print("The Sum is",Sum_of_Number)
    
def Factorial(Number):
    Factorial_of_Number = 1
    while Number > 1:
        for i in range(1,Number+1):
            Factorial_of_Number = Number * Factorial_of_Number 
            Number = Number - 1
    print("The factorial of the number is",Factorial_of_Number)

Take_Number = int(input("Enter the number "))
Sum(Take_Number)
Factorial(Take_Number)

