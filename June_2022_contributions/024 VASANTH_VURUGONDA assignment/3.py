import sys
import ast
#passing list using command line arguments
lst=sys.argv[1]
#converting input string to list using ast module
res=ast.literal_eval(lst)
print(res)
#printing reverse order of list using slicing technique
print(res[::-1])
#printing reverse order of list using reverse function
res.reverse()
print(res)