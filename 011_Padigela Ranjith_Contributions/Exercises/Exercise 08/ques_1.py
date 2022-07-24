"""
Write a script for factorial and take input 
from the command line parameter.
using while and for loops
"""

# Using while loop finding the factorial of given number.
num = int(input("Enter the number here: "))
prod = 1
while num > 0:
 prod *= num
 num -= 1
print(prod)

# Using for loop finding the factorial of given number.
p = 1
for i in range(1,num+1):
    p = p * i
print(p)