'''
This program prints birth day from current date stamp

'''
import datetime

ssb = '2022-11-23 00:00:00'
#b = '2022-07-24 16:20:22'
ct = str(datetime.datetime.now())

start = datetime.datetime.strptime(ssb, '%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(ct, '%Y-%m-%d %H:%M:%S.%f')

diff = start - ends

# ct stores current time
timenow = datetime.datetime.now()
print("current time: ", ct)

# ts store timestamp of current time
ts = timenow.timestamp()
print("timestamp: ", ts)

days = int(diff.days)
hours = int(diff.seconds // (60 * 60))
mins = int((diff.seconds // 60) % 60)
secs = int((diff.seconds%3600)%60)

print("Countdown for the birthday is:")

print("days: ", days)
print("hours: ", hours)
print("mins: ", mins)
print("secs: ", secs)

while True:
        # bd = input("Enter Birthdate in DDMMYYYY format:")
        
        try:
          bdc = datetime.datetime.strptime(input("Enter Birthdate in DDMMYYYY format:"), '%d%m%Y')
        except:
            print("Enter valid date!")
            continue
        # print('The date {} is valid.'.format(bd))
        diff2 = bdc - ends
        days = int(diff2.days)
        print("days left for bd:", days)

        
        
    

