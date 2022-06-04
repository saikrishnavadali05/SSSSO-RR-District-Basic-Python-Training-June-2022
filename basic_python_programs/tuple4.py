"""

Given a list of tuples. The task is to get all the tuples that have all 
positive elements.

Input :  [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
Output : [(4, 5, 9)] 
"""

#solution

# Python3 code to demonstrate working of
# Positive Tuples in List
# Using list comprehension + all()

# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

# printing original list
print("The original list is : " + str(test_list))

# all() to check each element
res = [sub for sub in test_list if all(ele >= 0 for ele in sub)]

# printing result
print("Positive elements Tuples : " + str(res))
