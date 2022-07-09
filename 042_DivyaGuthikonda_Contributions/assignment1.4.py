#Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
n=tuple(input(("Enter tuple: ")))
alt=list(n)
print(alt)
print(alt[::2])

#output
#Enter tuple: 02589630214
#['0', '2', '5', '8', '9', '6', '3', '0', '2', '1', '4']
#['0', '5', '9', '3', '2', '4']
