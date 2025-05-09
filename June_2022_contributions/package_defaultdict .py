#defaultdict()
'''The Python defaultdict() is defined as a dictionary-like object. It is a subclass of the built-in dict class. It provides all methods provided by dictionary but takes the first argument as a default data type.'''



from collections import defaultdict      
number = defaultdict(int)      
number['one'] = 1      
number['two'] = 2      
print(number['three'])    
