"""
Write a function that take three integers and compare 
which the largest and smallest among the them. take input from the end user.
"""

def Largest_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        lrg_num = num1
    elif num2 > num1 and num2 > num3:
        lrg_num = num2
    else:
        lrg_num = num3
    return lrg_num
def Smallest_num(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        Sml_num = num1
    elif num2 < num1 and num2 < num3:
        Sml_num = num2
    else:
        Sml_num = num3
    return Sml_num

print("Output is largest is ",Largest_num(20,10,65), "and smallest is",end=" ")
print(Smallest_num(20,5,65))
