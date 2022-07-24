# Find out what is a timestamp? Print date and time in a timestamp. Print the seconds, hours, minutes as sepearate integer numbers from that timestamp. (hint : use datetime module. Search on google when stuck).

# What is a timestamp?

# A timestamp is a sequence of characters or encoded
# information used to find when a particular event occurred,
# generally giving the date and time of the day, accurate 
# to a small fraction of a second.

import datetime as dt

# Printing current date and time using now() 
now = dt.datetime.now() # [YYYY-MM-DD HH:MM:SS Format]
print(now)

# Printing hours, minutes and seconds as seperate integers
print(now.hour)
print(now.minute)
print(now.second)