def Calculate(No1, No2):
    print("The sum is ",No1 + No2) 
    print("The multiplication is ",No1 * No2)
    if (No1 > No2):
        print("The Division is ",No1/No2)
        print("The Subtraction is ",No1 - No2)
    else:
        print("The Division is ",No2/No1)
        print("The Subtraction is ",No2 - No1)
    
Number1 = int(input("Enter any number "))
Number2 = int(input("Enter any number "))
Calculate(Number1,Number2)