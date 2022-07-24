# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:24:29 2021

@author: VIRAJ
"""

items=int(input("enter the number of items you bought:"))
if items>=1 and items<10:
    totalcost=items*12
    print("total cost of items in dollars is:",totalcost)
elif items>=10 and items<=99:
    totalcost=items*10
    print("total cost of items in dollars is:",totalcost)
elif items>=100:
    totalcost=items*7
    print("total cost of items in dollars is:",totalcost)