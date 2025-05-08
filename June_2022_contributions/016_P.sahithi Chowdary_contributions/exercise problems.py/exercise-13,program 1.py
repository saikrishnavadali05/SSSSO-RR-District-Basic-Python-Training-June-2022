set1 = {"maaza","sprite","fanta","maaza"}
set2 = {"pepsi","frooti","sprite","maaza"}
#set automatically deletes duplicate elements
print(set1)
set1.add("7-up")
print(set1)
u = set1.union(set2)
print("The union of two sets is ")
print(u)
i = set1.intersection(set2)
print("The intersection of two sets is")
print(i)
d = set2.difference(set1)
print("The difference of two sets")
print(d)
set2.remove("pepsi")
print(set2)



