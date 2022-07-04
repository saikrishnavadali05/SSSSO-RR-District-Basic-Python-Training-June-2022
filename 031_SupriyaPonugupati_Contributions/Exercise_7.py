# Write a script to check whether the given year is a leap year or not. The input i.e., year, 
# #should be given during script execution itself. i.e, as a command line parameter.

from sys import argv

input_year = int(argv[1])
if (input_year % 4 == 0):
    print("The year:", input_year, "is a leap year")
else:
    print("The year:",input_year,"is not a leap year")

#Write a script to check whether the given number is odd or even 
# by requesting input from the user, using input() function.

number = int(input("Enter the desired number"))
if (number % 2 == 0):
    print(" The number:",number,"is an even number")
else:
    print("The number",number, "is a odd number")

#Write a script that requests the user to give an input and given Kilometers convert to Miles.
#  if there are more digits after decimal round to two digits.

input_num = float(input("enter the km to be converted to miles"))
input_num = (input_num / 1.609)
print(" {:0.2f}.".format(input_num))

