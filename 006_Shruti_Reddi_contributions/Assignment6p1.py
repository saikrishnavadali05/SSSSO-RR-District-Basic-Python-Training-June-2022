# using time module
import time
  
# ts stores the time in seconds
ts = time.time()
  
# print the current timestamp
print(ts)

# using datetime module
import datetime;
  
# ct stores current time
ct = datetime.datetime.now()
print("current time:-", ct)
  
# ts store timestamp of current time
ts = ct.timestamp()
print("timestamp:-", ts)


from datetime import datetime
curr_dt = datetime.now()
 
print("Current datetime: ", curr_dt)
timestamp = int(round(curr_dt.timestamp()))
 
print("Integer timestamp of current datetime: ",timestamp)

# importing datetime module
from datetime import datetime 
 
# now is a method in datetime module is
# used to retrieve current data,time
myobj = datetime.now()
 
# printing current hour using hour
# class
print("Current hour ", myobj.hour) 
 
# printing current minute using minute
# class
print("Current minute ", myobj.minute)
 
# printing current second using second
# class
print("Current second ", myobj.second)
 
# printing current microsecond using
# microsecond class
print("Current microsecond ", myobj.microsecond)


# importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
  
# printing todays date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)