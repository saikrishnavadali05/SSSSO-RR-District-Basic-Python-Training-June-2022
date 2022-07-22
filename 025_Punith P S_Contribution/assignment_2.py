# program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)
number1 = 23
number2 = 34
if(number1 > number2):
    print("the maximum number is", number1)
else:
    print("the maximum number is" , number2)
    
if(number1 < number2):
    print("the minimum number is", number1)
else:
     print("the minimum number is", number2)
     
sum = number1 + number2
print("the addition of numbers is", sum)
average = sum / 2
print("the average of numbers is", average)