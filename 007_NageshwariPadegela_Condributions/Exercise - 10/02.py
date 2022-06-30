# Write a function that take three integers and compare which the largest and smallest among the them. take input from the end user.
'''
 example the given numbers are 45, 22, 60 
 - output is largest is 60 and smallest is 
'''

def max(a, b , c):
    if (a>b and a>c):
        largest = a
    elif (b>a and b>c):
        largest = b
    else:
        largest = c
    print("The largest among %d, %d, %d is %d"%(a, b, c, largest))

def min(a, b, c):
    if (a<b and a<c):
        smallest = a
    elif (b<a and b<c):
        smallest = b
    else:
        smallest = c
    print("The smallest among %d, %d, %d is %d"%(a, b, c, smallest))

number_1 = int(input("Enter a number of your choice: "))
number_2 = int(input("Enter a number of your choice: "))
number_3 = int(input("Enter a number of your choice: "))

maximum = max(number_1, number_2, number_3)

minimum = min(number_1, number_2, number_3)

