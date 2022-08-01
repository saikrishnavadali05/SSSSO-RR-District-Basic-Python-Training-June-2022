#Write a script to get the maximum and minimum value in a csv column containing 10 numbers. (hint : use pandas or csv libraries).
import pandas as pd
df=pd.read_csv('data.csv')
df=pd.DataFrame(index=['a','b','c','d','e'],coloumns=['x','y','z'])
a=df['Identifier'].max()
b=df['Identifier'].min()
print(a)
print(b)
