#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)

from audioop import reverse
from sys import argv

print("This program is to print list in reverse order")
list1 = argv[1:]
print("argument list :", list1)
print("The reverse list is :",list1 [::-1] )

