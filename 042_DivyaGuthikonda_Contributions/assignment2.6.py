#Find out what is a timestamp? Print date and time in a timestamp. 
# Print the seconds, hours, minutes as sepearate integer numbers from that timestamp.
# (hint : use datetime module. Search on google when stuck).

#  Timestamp is the pandas equivalent of python's Datetime and is interchangeable with it in most cases.
#  It's the type used for the entries that make up a DatetimeIndex, and other timeseries oriented data structures in pandas.
#  Parameters: ts_input : datetime-like, str, int, float.

from datetime import datetime
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%S:%H:%M")
print("Today's date:",date)
print("present time in seconds:hours:minutes format:",time)

#output
#Today's date: 23/07/2022
#present time in seconds:hours:minutes format: 02:11:52