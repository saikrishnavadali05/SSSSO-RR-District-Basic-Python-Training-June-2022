# Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

from sys import argv

list_items = argv[1]
distinct_set = set(list_items)
distinct_tuple = tuple(distinct_set)
sum = 0
for i in distinct_tuple:
    sum += eval(i)
print("Sum of all the elements of the distinct Tuple is", sum)