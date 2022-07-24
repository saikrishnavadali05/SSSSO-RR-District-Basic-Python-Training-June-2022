import datetime as dt

#Current Date and Time using now()
now = dt.datetime.now()
print(now)

#Creating datetime object
day = dt.datetime(2020, 9, 12)
print(day)

print(now.strftime('%B'))