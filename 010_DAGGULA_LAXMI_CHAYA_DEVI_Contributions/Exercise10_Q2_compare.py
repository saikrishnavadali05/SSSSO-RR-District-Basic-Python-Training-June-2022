#finding largest and smallest of three numbers using a function

def compare(num1,num2,num3):
   
    def largest(num1,num2,num3):
        if((num1>num2) and (num1>num3)):
           print("The largest number is",num1)
        elif((num2>num1) and (num2>num3)):
            print("The largest number is ",num2)
        else:
            print("The largest number is",num3)
    def smallest(num1,num2,num3):
        if((num1<num2) and (num1<num3)):
           print("The smallest number is",num1)
        elif((num2<num1) and (num2<num3)):
            print("The smallest number is ",num2)
        else:
            print("The smallest number is",num3)
    largest(num1,num2,num3)
    smallest(num1,num2,num3)
  


num1=int(input("Enter First number:"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number:"))
compare(num1,num2,num3)


