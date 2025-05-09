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

current_time = date2.strftime("%H:%M:%S")
print("Current Timestamp is =", current_time)

print("Countdown for the birthday is \n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
print()