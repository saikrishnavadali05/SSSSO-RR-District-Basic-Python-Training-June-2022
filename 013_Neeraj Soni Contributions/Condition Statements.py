#Condition Statements
#2

Integer = int(input("Write any number - "))
if (Integer% 2) == 0:
    print("the number is even")
else: print("the number is odd")

#3

inches = int(input("Please enter your height in inches: "))
feet1 = round(inches/12)
feet2 = inches%12
print(feet1,"feet", feet2, "inches")
