import csv

with open("university_records.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))
