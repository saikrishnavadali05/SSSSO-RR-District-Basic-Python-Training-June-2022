import datetime
from dateutil.relativedelta import relativedelta
a = '23-11-2022 00:00:00'
b = '24-07-2022 03:18:00'
start = datetime.datetime.strptime(a,'%d-%m-%Y %H:%M:%S')
ends = datetime.datetime.strptime(b,'%d-%m-%Y %H:%M:%S')
diff = relativedelta(start,ends)
print ("The difference is " %(diff.days,diff.months,diff.years,diff.hours,diff.minutes,diff.seconds ))