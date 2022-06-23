# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:22:26 2021

@author: VIRAJ
"""

num=int(input("enter the no. for which you want to find factorial:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial of given no. is:",factorial)