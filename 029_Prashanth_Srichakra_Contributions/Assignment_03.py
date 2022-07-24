# Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments
from sys import argv

list = argv[1]
rev_list = list[::-1]
print(rev_list)