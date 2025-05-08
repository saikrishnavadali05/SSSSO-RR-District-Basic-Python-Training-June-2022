# 3. Write a program to print all the elements within a list in the reverse order.
# The entire list has to be passed via command line arguments

from sys import argv


num1 = argv[1]
num2 = argv[2]
num3 = argv[3]
num4 = argv[4]
num5 = argv[5]

print('argv list:',argv[::-1])
