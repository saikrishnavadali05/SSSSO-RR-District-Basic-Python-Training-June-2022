from collections import OrderedDict 
  
od = OrderedDict()
od['c'] = 1
od['b'] = 2
od['a'] = 3
print(od.items())
d = {}
d['c'] = 1
d['b'] = 2
d['a'] = 3
print(d.items())

# Execute this on Python 2.7 compiler. The output would be as follows:
# [('c', 1), ('b', 2), ('a', 3)]
# [('a', 3), ('c', 1), ('b', 2)]
