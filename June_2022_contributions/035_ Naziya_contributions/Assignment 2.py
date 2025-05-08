# program to print maximum, minimum, average,addition,substraction of two numbers        
number1 = int(input("Give first number :",))
number2 = int(input("Give second number :",))
if(number1 > number2):
    print("maximum" , max(number1 , number2))
if(number2 < number1):
    print("minimum", min(number1 , number2))  
    print("addition", number1 + number2)
    print("multiplication" , number1 * number2)
    print("average", (number1 + number2)/2)
