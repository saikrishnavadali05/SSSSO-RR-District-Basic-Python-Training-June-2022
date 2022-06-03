"""
Given a Python list, write a program to remove all occurrences of item 10.

Given:
list1 = [5, 10, 15, 10, 25, 50, 10]

Expected output:
[5, 15, 25, 50]

"""

#solution

list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)










#solution

list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)