#Write a program to calculate number of days, hours, minutes, 
# seconds to the birthday of Sri Sathya Sai Baba from
#  the current timestamp(Birthday is on 23-November).
#a) Use datetime module.
import datetime

today= datetime.date.today().strftime("%d-%m-%Y")
print("The current day is :", today)
from datetime import date
from datetime import datetime
current_date = datetime.now()

print("The current timestamp is :", current_date)
x_date_time = datetime(year=2022, month=11, day=23, hour=00, minute=00)

# Difference between two dates
# Get timedelta
timedelta = x_date_time-current_date

print("The countdown for birthday is :", timedelta)
