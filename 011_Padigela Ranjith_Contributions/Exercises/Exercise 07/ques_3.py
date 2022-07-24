"""
Write a script that requests the user to give an input 
and given Kilometers convert to Miles.
if there are more digits after decimal round to two digits.
"""
# 1 Kilometer is equals to 0.621371 miles

km = float(input("Enter the Kilometers here: "))
km1 = round(km,2)
mile = km1 * 0.621371

print("The given Km of in  ",round(mile,2),"miles")