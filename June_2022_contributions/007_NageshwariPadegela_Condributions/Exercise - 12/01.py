# Write a python script that does the following operations:
# Input to the script will be a tuple with bike names : ("pulsar", "duke", "shine")
'''
*Script should* : 
1. give the total number of items present in the tuple.
2. give the index number for "shine" in the tuple.
3. add the item "splendor" to the tuple.
4. remove the item "duke" from the tuple.
'''

from operator import index


mytuple = ('pulsar', 'duke', 'shine')
print(mytuple)
print(type(mytuple))

# 1
print(len(mytuple))

# 2
print(mytuple.index('shine'))

# 3
mylist = list(mytuple)
mylist.append('splender')
mytuple = tuple(mylist)
print(mytuple)  

# 4
mylist = list(mytuple)
mylist.remove('duke')
mytuple = tuple(mylist)
print(mytuple)