# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:32:53 2021

@author: VIRAJ
"""

count1=0
count2=0
for i in range(1,101):
    if i**2%10==4:
        count1=count1+1
    if i**2%10==9:
        count2=count2+1
print("no. of numbers in 1 to 100 whose square end in 4 is:",count1)
print("no. of numbers in 1 to 100 whose square end in 9 is:",count2)