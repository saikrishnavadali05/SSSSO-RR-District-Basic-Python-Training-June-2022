'''
6.	Write a program to pass a list as a command line arguments.
Next, convert that list into a tuple after removing all the duplicate elements.
(hint : use set) Next, add all the elements of that duplicate free tuple
and print the addition output.

'''

from sys import argv

given_list = argv[1]
distinct_set = set(given_list)
to_tuple=tuple(distinct_set)

print("The duplicate free tuple is:", to_tuple)
sum = 0
for i in to_tuple:
    sum = sum + int(i)
print("Sum of elements of the tuple is:", sum)