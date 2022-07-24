"""
Write a script to print the count of number of digits within the given 
input number using while loop
"""

num = int(input("Enter the number here: "))
count = 0
while num > 0:
    rem = num % 10
    count += 1
    num //= 10
print(count)
