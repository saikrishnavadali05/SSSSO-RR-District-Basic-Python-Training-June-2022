from datetime import datetime, time

def date_in_seconds(dt2, dtt1):
    time = dt2-dtt1
    return time.days*24*3600 + time.seconds


def diff_seconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return(days, hours, minutes, seconds)


date1 = datetime.strptime('2022-11-23 00:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("current time stamp is ", date2)
print(" Countdown for birthday is \n%d days,%d hours,%d minutes,%d seconds" %
      diff_seconds(date_in_seconds(date2, date1)))
print()
