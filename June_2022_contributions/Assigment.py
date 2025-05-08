
from datetime import date

birth_year = int(input('When is your birthday? [YY] '))
birth_month = int(input('When is your birthday? [MM] '))
birth_day = int(input('When is your birthday? [DD] '))

Current_year = 2022 
Current_month = 7 
Current_day = 24 

Age_year = Current_year - birth_year
Age_month = Current_month - birth_month
Age_day = Current_day - birth_day

print(f"sri sathya baba exact age:{Age_year} years,{Age_month} month,{Age_day} day")




# Output
When is your birthday? [YY] 1926
When is your birthday? [MM] 11
When is your birthday? [DD] 23
1926-11-23 00:00:00 
sri sathya baba exact age:96 years,-4 month,1 day

