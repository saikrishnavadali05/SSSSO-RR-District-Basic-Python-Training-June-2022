#prog3
#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments

import sys
print("elements before reverse:",sys.argv)
print("after reverese:", sys.argv[1] [::-1])
