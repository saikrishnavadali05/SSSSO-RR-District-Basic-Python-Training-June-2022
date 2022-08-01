from datetime import datetime
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%S:%H:%M")
print("Current TimeStamp is",date,time)

def findAge(current_date, current_month, current_year, 
            birth_date, birth_month, birth_year):
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1]

    if (birth_month > current_month):         
        current_year = current_year - 1
        current_month = current_month + 12

    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    print( "Countdown for the Sri Sathya Sai Baba Birthday is :","Years:", calculated_year, "Months:",  
         calculated_month, "Days:", calculated_date)

current_date = 24
current_month = 7
current_year = 2022

birth_date = 23
birth_month = 11
birth_year = 2022
 
findAge(current_date, current_month, current_year, 
        birth_date, birth_month, birth_year)

#output
#Current TimeStamp is 24/07/2022 24:15:32
#Countdown for the Sri Sathya Sai Baba Birthday is : Years: -1 Months: 8 Days: 1