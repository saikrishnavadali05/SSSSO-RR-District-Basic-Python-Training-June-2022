set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}
print(set1)

set1.add("7_up")
print(set1)

combine = set1.union(set2)
print(combine)

diff = set2.difference(set1)
print(diff)

set2.remove("pepsi")
print(set2)