#Write a script to check whether the given year is a leap year or not. #
#The input i.e., year, should be given during script execution itself. i.e, 
#as a command line parameter.

#from sys import argv
#year1 = argv[1]
#if int(year1)%4==0:
   # print("the year is leap year", argv[1])
#else:
   # print("the year is not leap year", argv[1])

#Write a script to check whether the given number is odd or even 
#by requesting input from the user, using input() function.

#a = input("Enter a number")
#if int(a)%2==0:
    #print("Its an Even number") 
#else:
    #print("Its an Odd Number")

#Write a script that requests the user to give an input 
#which is a random value in inches and the script shall convert the inches value to feets and inches

a = input("Enter inches")
feet=divmod(int(a),12)
print(feet[0],"feet and",feet[1],"inches")
