import datetime as dt
from datetime import date

# Calculating Baba's Birthday

today = dt.datetime.now()
baba_bday = dt.datetime(2022,11,23,00,00,00)
bday = baba_bday - today

days = bday.total_seconds() // 86400
hrs = (bday.total_seconds() % 86400) // 3600
mins = (bday.total_seconds() % 3660) // 60
secs = bday.total_seconds() % 60

print("Current timestamp is", today, "and countdown for birthday is", bday.days,"days",hrs,"hours",mins,"mins",secs,"secs")


# Program to read input date in DDMMYYYY format. And calculate number of days to birthday.

today = date.today()
user_date = input("Enter date in DDMMYYYY format please: ")
if len(user_date)!=8:
    print("Enter a valid date please!")
else:
    user_year = int(user_date[4:8])
    user_mon = int(user_date[2:4])
    user_day = int(user_date[0:2])
    user_date = dt.date(user_year, user_mon, user_day)

    user_bday = user_date - date.today()
    print("Countdown for birthday is", user_bday.days,"days!!!")
