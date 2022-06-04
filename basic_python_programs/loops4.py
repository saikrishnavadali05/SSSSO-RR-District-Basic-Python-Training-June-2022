"""
Print downward Half-Pyramid Pattern with Star (asterisk)

pattern should be

* * * * *  
* * * *  
* * *  
* *  
*
"""


#solution

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")