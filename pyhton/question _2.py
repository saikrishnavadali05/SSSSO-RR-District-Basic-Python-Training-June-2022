import datetime

today= datetime.date.today().strftime("%d-%m-%Y")
print("The present day is :", today)
from datetime import date
from datetime import datetime
current_date = datetime.now()

print("The present timestamp is :", current_date)
date_time = datetime(year=2022, month=11, day=23, hour=00, minute=00)

# Difference between two dates
# Get timedelta
datetime = date_time-current_date

print("The countdown for birthday is :", datetime)