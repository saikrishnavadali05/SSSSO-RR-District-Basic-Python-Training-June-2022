"""
Write a script to print all the rows of a csv file. (hint : use pandas library).
"""

import pandas as pd

data = pd.read_csv(r"C:\Users\Padig\Downloads\COVID-19 Coronavirus.csv")

print(data)