"""
Check if two sets have any elements in common. If yes, display the common elements
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

"""


#solution

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))