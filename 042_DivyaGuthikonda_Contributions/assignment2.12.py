#Write a script to get the maximum and minimum value in a csv column containing 10 numbers. (hint : use pandas or csv libraries).
import pandas as pd
df=pd.read_csv('info.csv')
a=df['ColumnName'].max()
b=df['ColumnName'].min()
print(a)
print(b)