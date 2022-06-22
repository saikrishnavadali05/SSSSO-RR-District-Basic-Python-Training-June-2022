# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:39:25 2021

@author: VIRAJ
"""

n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+1/(i*i)
print("the value of the sequence is:",sum)