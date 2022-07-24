from Assignment-24-7-22 import Add
from Assignment-24-7-22 import multiple
Number = list(input("Enter the numbers "))

Even = []
Length = len(Number)

print("The number of Digits are",len(Number))
if len(Number) == 4:
    for i in range(0,len(Number)):
        if(int(Number[i]) % 2 == 0):
            Digits = Digits + 1
            Add = Number[i]
            Even.append(Add)
            print("The Even Numbers are", Even)
        else:
            print("No Even Numbers found")
    else:
        print("Enter four numbers")

    Add(Digits,Even)
    multiple(Digits,Even)