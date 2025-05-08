#12.Write a script to get the maximum and minimum value in a csv column containing 10 numbers. (hint : use pandas or csv libraries).
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                   "B":[5, 2, 54, 3, 2], 
                   "C":[20, 16, 7, 3, 8], 
                   "D":[14, 3, 17, 2, 6]})
print(df.min(axis=0))
print(df.max(axis=0))