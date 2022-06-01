"""
If a mutable object is called by reference in a function, it can change the 
original variable itself. Hence to avoid this, the original variable needs 
to be copied to another variable. The list is called via call by reference, 
so the changes are made to the original list itself. 
"""

def updateList(list1):
  list1 += [10]

n = [5, 6]
print(n, id(n))                 
updateList(n)
                    
print(n, id(n)) 

print("-----------")

"""
Immutable objects can be called by reference because its value cannot be 
changed anyways.
"""

def updateNumber(n):
  print(id(n))
  n += 10
  print(n, id(n))

b = 5
print(b, id(b))                  
updateNumber(b)                
print(b, id(b))                 
