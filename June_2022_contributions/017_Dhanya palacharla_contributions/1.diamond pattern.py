# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:45:42 2021

@author: VIRAJ
"""

n=int(input("enter the height of diamond:"))
a=1
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*a)
    a=a+2
c=a
b=c-2
while(b>0):
    for i in range(1,n+1):
        print(' '*i,end='')
        print('*'*b)
        b=b-2