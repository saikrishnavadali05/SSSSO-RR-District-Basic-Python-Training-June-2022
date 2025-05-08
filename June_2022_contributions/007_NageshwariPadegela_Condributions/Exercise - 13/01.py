# Write a python script that takes the following two sets as inputs and does the following operations on those sets :
# Input Sets :
'''
set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}
 Operations to be done on those Sets :
 1. Remove the duplicate elements from the set1.
 2. Add an item "7_up" to the set1.
 3. Compute the union and intersetion of set1 and set2.
 4. Compute the difference of set1 from set2.
 5. Then remove the "pepsi" element from the set2.
 '''

set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}

# 1
print(set1)
print(set2)

# 2
set1.add('7_up')
print('set1: ',set1)

# 3
print('Union of set1 and set2 is: ', set1|set2)
print('Intersection of set1 and set2 is: ', set1 & set2)

# 4
print('Difference of set1 from set2 is: ', set1-set2)

# 5
set2.remove('pepsi')
print('set2: ', set2)
