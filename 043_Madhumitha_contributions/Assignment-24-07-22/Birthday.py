import datetime
from sqlite3 import Date

rules = {0: "Monday",
         1: "Tuesday",
         2: "Wednesday",
         3: "Thursday",
         4: "Friday",
         5: "Saturday",
         6: "Sunday"}


class Time(object):
    now = datetime.datetime.now()

    def __init__(self, year=1, month=1, Date=1, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, Date, hour, minute, second)

today = Time().now
birthday = Time(2022,11,23).date

def exception():
    try:
        Date == "YYYYDDMM"
        print(birthday)

    except :
        print("The date format provided is invalid. Please provide input in YYYYMMDD format ")

def day_of_week():
    return "Today is %s" % rules[today.weekday()]


def birthday_stats(birthday):
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1

    birthday_ = Time(today.year, birthday.month, birthday.day).date
    till_birthday = str(birthday_ - today).split()

    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print ("You are %s years old" % (age))
    ct = datetime.datetime.now()
    print("current time:", ct)
    print("Countdown for next Birthday is : %sd:%sh:%sm:%ss until your next birthday."
    % (days, hours, mins, secs)) 

print(day_of_week())
birthday_stats(birthday)


