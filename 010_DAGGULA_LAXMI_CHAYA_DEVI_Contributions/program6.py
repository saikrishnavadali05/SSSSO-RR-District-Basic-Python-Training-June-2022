#converting list to tuple
import ast
import sys
#getting list using command line arguments
lst=sys.argv[1]
print(lst)
lst=ast.literal_eval(lst)
#removing duplicate from list
new_lst=list(set(lst))
print(new_lst)
#converting list to tuple
tpl=tuple(new_lst)
print(tpl)
#adding elements in tuple
sum=0
for i in tpl:
    sum+=i
print(sum)