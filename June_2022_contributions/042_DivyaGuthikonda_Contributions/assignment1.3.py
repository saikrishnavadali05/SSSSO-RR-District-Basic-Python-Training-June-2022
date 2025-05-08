#(It's incomplete)
#Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments
'''
from sys import argv

str = argv[1]
rev=str[::-1]
print("reverse of a string: ",rev)
'''
import sys
for arg in sys.argv:
    print("the name of file is :",arg)
#the name of file is : assignment1.3.py