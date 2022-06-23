# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:41:29 2021

@author: VIRAJ
"""

for i in range(1,1000):
    a=0
    for j in range(1,i):
        if i%j==0:
            a=a+j
    if i==a:
            print(i)