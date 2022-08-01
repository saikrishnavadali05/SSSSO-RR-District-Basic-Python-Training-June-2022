from datetime import datetime
def ageCalculator(years,months,days,year,month,date):
    import datetime
    today=datetime.date(years,months,days)
    dob=datetime.date(year,month,date)
    years=((today-dob).total_seconds()/(365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*12
    monthsInt=int(months)
    daysInt=int(days)
    print('You are {0} years, {1} months, {2} days old'.format(yearsInt,monthsInt,daysInt))


birthdate=input("Enter your birthdate(yyyy-mm-dd): ")  
my_dt=datetime.strptime(birthdate, "%Y-%m-%d")  
b_yr=my_dt.year
b_mnth=my_dt.month
b_dt=my_dt.day
now=datetime.now()
c_yr=int(now.strftime("%Y"))
c_mnth=int(now.strftime("%m"))
c_dt=int(now.strftime("%d"))
ageCalculator(c_yr,c_mnth,c_dt,b_yr,b_mnth,b_dt)