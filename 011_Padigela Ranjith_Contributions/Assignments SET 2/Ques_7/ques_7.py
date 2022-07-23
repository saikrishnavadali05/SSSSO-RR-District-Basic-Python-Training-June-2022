"""
Given a string print all the lowercase characters, 
upper case characters and numeric characters and their counts.
"""

strng = input("Enter the string here : ")

upcnt  =  0
lwcnt  =  0
numcnt =  0
lstU = []
lstL = []
lstN = []
for i in strng:
    if i.isupper():
        upcnt += 1
        lstU.append(i)
for j in strng:
    if j.islower():
        lwcnt += 1
        lstL.append(j)
for k in strng:
    if k.isnumeric():
        numcnt += 1
        lstN.append(k)

print("Uppercase",lstU,"count is ",upcnt)
print("Lowercase",lstL,"count is ",lwcnt)
print("Numeric",lstN,"count is ",numcnt)
