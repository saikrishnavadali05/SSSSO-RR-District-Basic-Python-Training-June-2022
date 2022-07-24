import csv 
Details = ['Name', 'class', 'passoutYear', 'subject']  
rows = [ ['sushma', '2nd', '2023', 'Physics'],  ['john', '3rd', '2022', 'M2'],  ['kushi', '4th', '2021', 'M4']] 
with open('Assignment_2_2.13.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(Details) 
    write.writerows(rows) 