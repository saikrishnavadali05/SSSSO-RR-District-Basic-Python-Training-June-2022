# Input Sets :
set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}
# removing duplicates and printing set
# set considers only unique elements it does not consider any duplicates
print(set1)
# adding an item 7_up to set1
set1.add("7_up")
print(set1)
# union of set1 and set2
print("Union of set1 and set2 :", set1 | set2)
# intersection of set1 andd set2
print("intersection of set1 and set2", set1 & set2)
# difference of set1 from set2
print("difference:", set2-set1)
# removing "pepsi" element from set2
set2.remove("pepsi")
print(set2)
