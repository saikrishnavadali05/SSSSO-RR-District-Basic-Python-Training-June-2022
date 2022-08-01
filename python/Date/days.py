from datetime import datetime
from datetime import date
import time

today = date.today()

def user_birthday():
    day = int(input('When is your birthday? [DD] '))
    month = int(input('When is your birthday? [MM] '))
    year = int(input('When is your birthday? [YY] '))

    birthday = datetime(year,month, day)
    return birthday

def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday


bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t-today)
days=str(time_to_birthday.days)
print("Time to Birthday is :" + days + " days")
