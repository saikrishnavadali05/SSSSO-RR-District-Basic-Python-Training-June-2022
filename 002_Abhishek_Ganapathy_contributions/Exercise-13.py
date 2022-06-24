# Write a python script that takes the following two sets as inputs and does the following operations on those sets
set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}

print("The Set1 is", set1)
set1.add("7_up")
print("The modifed setup1 after 7_up is", set1)
set3 = set1.union(set2)
print("The combination of set1 and set2 is", set3)
print("The difference between 2 sets set1 and set2")
print("set1 - set2",set1-set2)
print("set2 - set1",set2-set1)
set2.remove("pepsi")
print("The set2 after removing pepsi is",set2)