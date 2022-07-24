# Input Sets :
from ctypes import Union


set1 = {"maaza", "sprite", "fanta", "maaza"}
set2 = {"pepsi", "frooti", "sprite", "maaza"}

#1
print(set1)
#{'maaza', 'sprite', 'fanta'}
 
#2
set1.add("7_up")
print(set1) #{'fanta', '7_up', 'maaza', 'sprite'}

#3.a
print(set1.union(set2))
#{'fanta', '7_up', 'maaza', 'sprite'}

#3.b
print(set1.intersection(set2))
#{'sprite', 'maaza'}

#4
print(set2.difference(set1))
#{'pepsi', 'frooti'}

#5
set2.remove("pepsi")
print(set2)
#{'frooti', 'maaza', 'sprite'}