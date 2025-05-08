#2. Write a program to calculate number of days, hours, minutes, seconds to the birthday of Sri Sathya Sai Baba from the current timestamp(Birthday is on 23-November). 
#	a) Use datetime module. 
#	d) Also, create a program to read input date in DDMMYYYY format. And calculate number of days to birthday.
#	e) The program must also  handle the errors. For eg., if date given is 20-May-2022, the program must throw error and send message to user - 'The date format provided is invalid. Please provide input in DDMMYYYY format' 
#	f) The program must also be able to handle future dates greater than 23112022 and throw a message to the user to input a date less than 23112022.
#Solution 1:
from datetime import datetime, time

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

#Specified date
date1 = datetime.strptime('2022-11-23 00:00:00', '%Y-%m-%d %H:%M:%S')


#Current date
date2 = datetime.now()

print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
print()


#solution 2
from datetime import datetime

def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(2000+year,month,day)
    return birthday

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days

bd = get_user_birthday()
now = datetime.now()
c = calculate_dates(bd, now)

print(c)


#solution 3:
import datetime


def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime.datetime(year,month,day)
    return birthday


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta = date2 - date1
    days = delta.total_seconds() / 60 /60 /24

    return days


def show_info(self):
    pass



bd = get_user_birthday()
now = datetime.datetime.now()
c = calculate_dates(bd,now)
print(c)
