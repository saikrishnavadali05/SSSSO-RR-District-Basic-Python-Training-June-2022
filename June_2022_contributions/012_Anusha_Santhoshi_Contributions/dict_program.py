# Declaring a dict variable with multiple string variable in it  
ADict = {'mkr1': 'at',  
               'mkr2': 'JavaTpoint',   
               'mkr3': 'Learning',  
               'mkr4':'operator',  
               'mkr5':'concept',  
               'mkr6': '%s'}  
# Mapping a string with string variables in dictionary  
ResultantStr = "%(mkr3)s %(mkr6)s %(mkr4)s %(mkr5)s %(mkr1)s %(mkr2)s" % ADict  
# Printing result in output  
print("Resultant mapped string with ordered variable from dictionary: ")   
print(ResultantStr)  