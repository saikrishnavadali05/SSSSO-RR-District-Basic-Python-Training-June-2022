def Multiply(Digits,Even):
    Sum_of_Multiplication = 1
    for i in range(0,Digits):
        Sum_of_Multiplication = int(Even[i]) * Sum_of_Multiplication
    print("The multiplication is",Sum_of_Multiplication)
