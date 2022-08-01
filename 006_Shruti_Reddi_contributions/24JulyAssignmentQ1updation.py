
from add import *
from multiply import *

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Multiply")
 
# Take input from the user
select = int(input("Select operations form 1, 2,:"))
# take input from the user
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
number3 = int(input("Enter 3rd number: "))
number4 = int(input("Enter 4th number: "))


# check if choice is one of the two options
if select == 1:
    #check for the number to be even 
     if (number1 % 2 == 0 and number2 %2==0 and number3 % 2==0 and number4 %2==0):
           print("The addition of numbers is :", (add(number1, number2, number3, number4)))
     else:
          print("The numbers are odd")
elif select==2:
    if (number1 % 2 == 0 and number2 %2==0 and number3 % 2==0 and number4 %2==0):
        print("The multiplication of numbers is :", (multiply(number1, number2, number3, number4)))
    else:
          print("The numbers are odd")
else:
    print("Invalid input")

with open("Output1.txt", "w") as fp:
  fp.write(str((add(number1,number2,number3,number4))))
  fp.write(str(multiply(number1,number2,number3,number4)))
fp.close()