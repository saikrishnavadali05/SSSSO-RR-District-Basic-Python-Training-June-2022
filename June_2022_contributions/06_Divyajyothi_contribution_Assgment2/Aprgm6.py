#6.Find out what is a timestamp? Print date and time in a timestamp.
#  Print the seconds, hours, minutes as sepearate integer numbers from that timestamp.
#  (hint : use datetime module. Search on google when stuck).

from datetime import datetime
from datetime import timedelta
present_dt = datetime.now()
print("Current date,time is : ", present_dt)
timestamp = int(round(present_dt.timestamp()))
print("Integer timestamp of current date,time in seconds is : ", timestamp)
td_str = str(timedelta(seconds=timestamp))
x = td_str.split(':')
print('Time in days:hh:mm:ss is :', x[0], 'Hours', x[1], 'Minutes', x[2], 'Seconds')