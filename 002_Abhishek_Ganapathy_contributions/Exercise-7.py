print("question 1")
from sys import argv
year = int(argv [1])
if (year % 4 == 0):
    print(year, "This is a leap year")
else:
    print(year, "Is not a leap year")
    
print("question 2")
number1 = int(input("Provide a number "))
if(number1 % 2 == 0):
    print(number1,"is even")
else:
    print(number1, "is odd")

print("question 3")
To_convert = float(input("Enter the inches "))
feet = int(To_convert/12)
inches = int(To_convert % 12)
print(To_convert,"is equal to",feet,"feet",inches,"inches") 
