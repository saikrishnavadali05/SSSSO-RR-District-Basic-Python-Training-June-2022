import os

# eval() interprets a string as code
# eval with input() is a security hole and in many other cases where 
# input could come from file etc

eval(input(""Enter data: "))   # os.system('dir')