# Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
tup = tuple(input("Enter tuple elements:"))
print("Alternate elements in the tuple are:")
alt_tup = tup[::2]
for i in alt_tup:
    print(i, end=" ")