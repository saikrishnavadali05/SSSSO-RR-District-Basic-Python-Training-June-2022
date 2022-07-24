import datetime;
td=datetime.date(2022,11,23)
print(td)
tm = datetime.time(00, 00, 00, 00)
print(tm)
ct = datetime.datetime.now()
print("current date time:-", ct)
print("current month:-", ct.month)
print("current year:-", ct.year)
print("Current hour =", ct.hour)
print("Current minute =", ct.minute)
print("Current second =", ct.second)

ts = ct.timestamp()
print("timestamp:-", ts)

from datetime import datetime

i = str(input())
try:
    dt_start = datetime.strptime(i, '%Y, %m, %d')
except ValueError:
    print("Incorrect format")