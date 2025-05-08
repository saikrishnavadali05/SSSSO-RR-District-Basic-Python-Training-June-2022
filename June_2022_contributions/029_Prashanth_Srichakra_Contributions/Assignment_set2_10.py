# Write a script to print all the rows of a csv file.

# Note:
# A CSV file (Comma Separated Values file) is a type of plain text file 
# that uses specific structuring to arrange tabular data. 

import csv
import pandas as p

# Reading CSV File using csv module

print('Reading csv file using csv module')

row_count = 0
with open("csv_file.txt") as csvf:
    csv_reader = csv.reader(csvf, delimiter=',')
    for r in csv_reader:
        print(f'row {row_count} elements are {", ".join(r)}')
        row_count += 1

print()

# Reading CSV File using pandas module
print('Reading csv file using pandas module')

csv_data = p.read_csv("csv_file.txt")
print(csv_data.to_string())