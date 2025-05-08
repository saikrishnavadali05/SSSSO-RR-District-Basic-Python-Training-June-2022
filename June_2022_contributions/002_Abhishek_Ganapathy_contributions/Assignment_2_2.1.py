def add(Number):
    Sum = 0
    while Number > 0:
        Remainder = Number % 10
        Sum = Remainder + Sum
        Number = Number // 10
    print("The sum of the number is ",Sum)   
        
def Difference(Number):
    Difference = 0
    while Number > 0:
        Remainder = Number % 10
        if(Difference > Remainder):
            Difference = Difference - Remainder
        else:
            Difference = Remainder - Difference
        Number = Number // 10
    print("The Difference of the number is ",Difference) 

def Multiply(Number):
    MultiplySum = 1
    while Number > 0:
        Remainder = Number % 10
        MultiplySum = MultiplySum*Remainder
        Number = Number // 10
    print("The multiplication of the number is ",MultiplySum)

def Division(Number):
    DivisionSum = 1
    while Number > 0:
        Remainder = Number % 10
        if(Remainder > DivisionSum):
            DivisionSum = Remainder/DivisionSum
        else:
            DivisionSum = DivisionSum/Remainder
        Number = Number // 10
    print("The Division of the number is ",DivisionSum)

GetNumber = int(input("Enter the number "))
add(GetNumber)
Difference(GetNumber)
Multiply(GetNumber)
Division(GetNumber)

