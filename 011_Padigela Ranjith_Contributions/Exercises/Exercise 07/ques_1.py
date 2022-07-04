"""
Write a script to check whether the given year is a leap year or not.
The input i.e., year,should be given during script execution itself.
i.e, as a command line parameter.
"""
from sys import argv

year = argv[1]

if int(year) % 4 == 0 and  int(year) % 100 != 0 or int(year) % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year") 