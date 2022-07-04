'''The Python OrderedDict() is similar to a dictionary object where keys maintain the order of insertion. If we try to insert key again, the previous value will be overwritten for that key.'''

import collections    
d1=collections.OrderedDict()    
d1['A']=10    
d1['C']=12    
d1['B']=11    
d1['D']=13    
    
for k,v in d1.items():    
    print (k,v)   
