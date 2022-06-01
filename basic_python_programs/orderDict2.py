from collections import OrderedDict 
  
print("Before:") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items(): 
  print(key, value) 
  
print("\nAfter:") 
od['c'] = 5
for key, value in od.items(): 
  print(key, value) 
