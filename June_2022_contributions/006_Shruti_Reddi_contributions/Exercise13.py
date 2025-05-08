#Write a python script that takes the following two sets as inputs and does the following operations on those sets :
# Input Sets :
set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}
#Operations to be done on those Sets :
#1. Remove the duplicate elements from the set1.
print(set1)
#2. Add an item "7_up" to the set1.
set1.add("7 up")
print(set1)
#3. Compute the union and intersetion of set1 and set2.
union_set= set1.union(set2)
print(union_set)

intersection_set=set1.intersection(set2)
print(intersection_set)
#4. Compute the difference of set1 from set2.
difference_set=set2.difference(set1)
print(difference_set)
#  #5. Then remove the "pepsi" element from the set2.
set2.remove("pepsi")
print(set2)