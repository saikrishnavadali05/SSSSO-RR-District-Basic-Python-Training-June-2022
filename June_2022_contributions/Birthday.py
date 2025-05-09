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
my_date=datetime.strptime(birthdate, "%Y-%m-%d")  
b_year=my_date.year
b_month=my_date.month
b_date=my_date.day
now=datetime.now()
c_year=int(now.strftime("%Y"))
c_month=int(now.strftime("%m"))
c_date=int(now.strftime("%d"))
ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)
