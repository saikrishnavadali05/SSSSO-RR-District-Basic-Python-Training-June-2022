# QUESTION -1 solution 
# by KARPAGA NANTHINI S
# Om Sai ram!

from add import addnumbers
from multiply import mulnumbers

def main_():
    operation=str(raw_input("Enter the operation to be performed: \n"))
    #print (operation)

    if operation == "add":
        num1=int(input("Enter the number 1:"))
        num2=int(input("Enter the number 2:"))
        num3=int(input("Enter the number 3:"))
        num4=int(input("Enter the number 4:"))
        print("The add operation is performed now!!!")
        addnumbers(num1,num2,num3,num4)
    elif operation == "mul":
        num1=int(input("Enter the number 1:"))
        num2=int(input("Enter the number 2:"))
        num3=int(input("Enter the number 3:"))
        num4=int(input("Enter the number 4:"))
        print("The multiply operation is performed now!!!")
        mulnumbers(num1,num2,num3,num4)
    else:
        print ("No proper operation selected!!!")

main_()