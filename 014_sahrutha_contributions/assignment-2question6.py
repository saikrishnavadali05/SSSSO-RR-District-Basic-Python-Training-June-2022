from datetime import datetime
from datetime import timedelta
# present time
present_dt = datetime.now()

print("Current datetime: ", present_dt)
timestamp = int(round(present_dt.timestamp()))

print("Integer timestamp of current datetime in seconds: ", timestamp)
td_str = str(timedelta(seconds=timestamp))
# split string into individual component
x = td_str.split(':')
print('Time in hh:mm:ss:', x[0], 'Hours', x[1], 'Minutes', x[2], 'Seconds')