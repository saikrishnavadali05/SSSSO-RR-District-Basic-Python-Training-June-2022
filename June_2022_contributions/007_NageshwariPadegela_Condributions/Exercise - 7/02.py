# Write a script to check whether the given number is odd or even\
#  by requesting input from the user, using input() function.

number = int(input("Enter a number of your choice: "))

if number%2 == 0:
    print('The number %d is a even number'%number)
else:
    print('The number %d is a odd number'%number)
    