"""
Removal all characters from a string except integers

Given:
str1 = 'I am 25 years and 10 months old'

output

2510
"""

#solution

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)