from collections import OrderedDict 
  
print("Before deleting:") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
  print(key, value) 
  
print("\nAfter deleting:") 
od.pop('c') 
for key, value in od.items(): 
  print(key, value) 
  
print("\nAfter re-inserting:") 
od['c'] = 3
for key, value in od.items(): 
  print(key, value)