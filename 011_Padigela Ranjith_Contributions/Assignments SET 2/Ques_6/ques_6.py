"""
Python provides the various libraries to work with timestamp data.
For example,the datetime and time module helps in handling the multiple dates and
time formats.

The timestamp() method of a datetime module returns the POSIX timestamp
corresponding to the datetime instance. The return value is float.
"""
from datetime import datetime

ct = datetime.now() # Printing the current date using the datetime module.

ts = datetime.timestamp(ct) # Converting the current date and time into timestamp

print("Printing the timestamp here : ",ts)
tsf = datetime.fromtimestamp(ts) # Im retrieving the date and time from the timestamp using fromtimestamp method in datetime module.
date = tsf.strftime("%D-%B-%Y")
time = tsf.strftime("%H:%M:%S")
print("Printing the date :",date)
print("Printing the time :",time)

h = tsf.strftime("%H")
m = tsf.strftime("%M")
s = tsf.strftime("%S")

print("Printing the hour here",h)
print("Printing the minute here",m)
print("Printing the seconds here",s)


