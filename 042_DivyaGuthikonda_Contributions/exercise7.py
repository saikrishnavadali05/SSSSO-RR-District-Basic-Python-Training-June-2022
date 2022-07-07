#Write a script to check whether the given year is a leap year or not. The input i.e., year, should be given during script execution itself. i.e, as a command line parameter.
year=int(input("Enter Year :"))
if (year%4 == 0):
 print("The given year is a leap year")
else:
    print("The given year is not a leap year")
#Enter Year :2024
#The given year is leap year

#Write a script to check whether the given number is odd or even by requesting input from the user, using input() function.
number=int(input("Enter the Number :"))
if(number%2==0):
 print("The given number is even number")
else:
 print("The number is odd number")
#Enter the Number :57           #Enter the Number :56
#The number is odd number       #The given number is even number

#Write a script that requests the user to give an input and given Kilometers convert to Miles. if there are more digits after decimal round to two digits.
kilometer=float(input("Enter Kilometers :"))
mile=kilometer*0.621
print("after converting kilometer to miles :",round(mile,2))
#Enter Kilometers :26
#after converting kilometer to miles : 16.15

#(if we wanna enter floating point then mention float at input line)
#Enter Kilometers :4.8
#after converting kilometer to miles : 2.98