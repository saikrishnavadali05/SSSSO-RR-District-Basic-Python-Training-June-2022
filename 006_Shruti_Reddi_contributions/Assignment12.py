#Write a script to get the maximum and minimum value 
# in a csv column containing 10 numbers. 
# (hint : use pandas or csv libraries).


import csv 
    
# field names 
fields = ['Numbers'] 
    
# data rows of csv file 
rows = [ ['10'], 
         ['2'], 
         ['355'], 
         ['40'], 
         ['500'], 
         ['6'],['75'],['18'],['91'],['100']] 
    
# name of csv file 
filename = "numbers_minmax.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

import pandas as pd
df=pd.read_csv('numbers_minmax.csv')


#FINDING MAX AND MIN
p=df['Numbers'].max()
q=df['Numbers'].min()

print(p)
print(q)
