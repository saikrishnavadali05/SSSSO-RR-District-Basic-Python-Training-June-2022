def add(Number):
    Sum = 0
    Remainder = 0
    while Number > 0:
        Remainder = Number % 10
        Sum = Remainder + Sum
        Number = Number // 10
    print("The sum of the number is ",Sum)
    File_input = open("Assignment_2_2.1b_Output.txt","w")
    File_input.write("The Sum of the number is ")
    File_input.write(str(Sum))  
    File_input.close()
        
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
    File_input1 = open("Assignment_2_2.1b_Output.txt","a")
    File_input1.write("\nThe Difference of the number is ")
    File_input1.write(str(Difference))  
    File_input1.close()

def Multiply(Number):
    MultiplySum = 1
    while Number > 0:
        Remainder = Number % 10
        MultiplySum = MultiplySum*Remainder
        Number = Number // 10
    print("The multiplication of the number is ",MultiplySum)
    File_input2 = open("Assignment_2_2.1b_Output.txt","a")
    File_input2.write("\nThe Multiplication of the number is ")
    File_input2.write(str(MultiplySum))  
    File_input2.close()

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
    File_input3 = open("Assignment_2_2.1b_Output.txt","a")
    File_input3.write("\nThe Division of the number is ")
    File_input3.write(str(DivisionSum))  
    File_input3.close()

with open("Assignment_2_2.1b_Input.txt") as File_input:
    number = File_input.read()
    Convert_Number = int(number)
    print(Convert_Number) 

add(Convert_Number)
Difference(Convert_Number)
Multiply(Convert_Number)
Division(Convert_Number)

