#excercise 7

#Write a script to check whether the given year is a leap year or not. The input i.e., year, should be given during script execution itself. i.e, as a command line parameteers

year = int(input("enter the year"))
print(year)
if (year % 4 == 0):
    print("{0} is  a leap year :" .format(year))
else:
    print("{0} is not  a leap year :" .format(year))
 
 # Write a script to check whether the given number is odd or even by requesting input from the user, using input() function.

number = int(input("enter the number"))
if (number % 2 != 0):
    print(number , " is odd")
else:
    print(number , " is even")

#Write a script that requests the user to give an input and given Kilometers convert to Miles. if there are more digits after decimal round to two digits

kilometers = float(input("enter the number of kilometers")) 
convert = 0.621
no_miles = kilometers * convert
print(no_miles , round(no_miles , 2) )

