# Program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.

# For integers tuple
x = input('Enter the tuple with integers: ')
x = tuple(int(a) for a in x.split(","))
print(x[::2])

# For sting tuple 
x = input('Enter the tuple with strings: ')
x = tuple(str(a) for a in x.split(","))
print(x[::2])

# For mixed tuple
x = input('Enter the tuple : ')
x = tuple((a) for a in x.split(","))
print(x[::2])

