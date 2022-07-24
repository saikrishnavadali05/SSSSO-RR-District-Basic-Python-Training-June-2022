#Adding and multiplying only even numbers from the given input numbers
from add import addition
from multiply import multiplication
n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))
n4 = int(input("Enter the fourth number"))
if(n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2!=0):
    import sys
    sys.stdout = open(r'C:\Users\Dell\Desktop\python files\assignment 1st problem output.txt',"a")
    print("There is no even number in the given input")
else:    
 s = addition(n1,n2,n3,n4)
 m = multiplication(n1,n2,n3,n4)
 import sys
 sys.stdout = open(r'C:\Users\Dell\Desktop\python files\assignment 1st problem output.txt',"a")
 print("The addition of the even numbers is ",s)
 print("The multiplication of the even numbers is ",m)
