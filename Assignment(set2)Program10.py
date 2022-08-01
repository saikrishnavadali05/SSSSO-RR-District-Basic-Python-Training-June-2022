#10.Write a script to print all the rows of a csv file. (hint : use pandas library).
import pandas as pd
df=pd.read_csv(r"C:\Users\UDAY\Downloads\datasets_r_programming\customer_churn.csv")
print(df)
# for printing rows in a data set
pd.set_option('display.max_rows', None)
df = pd.read_csv(r"C:\Users\UDAY\Downloads\datasets_r_programming\customer_churn.csv")
print(df)