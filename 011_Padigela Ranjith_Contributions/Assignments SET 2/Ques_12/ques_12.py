"""
Write a script to get the maximum and minimum value in a 
csv column containing 10 numbers. (hint : use pandas or csv libraries).
"""
import pandas as pd

DataFrame = pd.read_csv(r"C:\Users\Padig\Downloads\salary.csv")
maximum_value = DataFrame[:].max()
print(maximum_value)
print("-----------------------------")
minimum_value = DataFrame[:].min()
print(minimum_value)