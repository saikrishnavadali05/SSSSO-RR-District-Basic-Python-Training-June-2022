from datetime import date
d=list(map(int,input("Enter your date-month-year:").split("-")))
date1=date(d[2],d[1],d[0])
date2=date(2022,11,23)
if(date1>date2):
    print("Date must be less than 23-11-2022")

elif((d[0] not in range(1,32))or d[1] not in range(1,13)):
    print("invalid input enter in the form of date-month-year")
else:
    f=date2-date1
    print("difference in days is ",f.days)
    print("differnce in hours is ",f.days*24)
    print("differnce in minutes is ",f.days*1440)
    print("differnce in seconds is ",f.days*86400)
    

