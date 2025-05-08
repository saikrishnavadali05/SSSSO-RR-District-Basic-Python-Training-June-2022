# Write a script to check whether the given year is a leap year or not.\
# The input i.e., year, should be given during script execution itself.\
#  i.e, as a command line parameter.

from sys import argv 
year = argv[1]
if ((int(year)%4 == 0 and int(year)%100 != 0) or (int(year)%400 == 0)):
    print('The year %s is a leap year'%year)
else:
    print('The year %s is not a leap year'%year)



'''
year%4 == 0 - leap
year%4 == 0 and year%100 != 0 - leap year
year%100 == 0 and year%400 == 0 -leap year
'''