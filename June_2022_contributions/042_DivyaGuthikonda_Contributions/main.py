from add import *
from multiply import *
from sys import argv
try:
    a=int(input("Give first number: "))
    b=int(input("Give second number: "))
    c=int(input("Give third number: "))
    d=int(input("Give fourth number: "))
    add()
    multiply()
except:
    print("Error: Provide four numbers.")
f=open("file_output.txt","a")
print("The data that is storing in this text file :",file=f)
print("addition of given numbers: ",add(a,b,c,d),file=f)
print("multiplication of given numbers: ",multiply(a,b,c,d),file=f)
f.close()

#output
#Give first number: 3
#Give second number: 4
#Give third number: 5
#Give fourth number: 6