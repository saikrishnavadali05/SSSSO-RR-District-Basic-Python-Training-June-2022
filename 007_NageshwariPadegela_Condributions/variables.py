# A variabel is an alternative name for the memory Location and 
# they act as containers for storing the data values.

'''Rules for Python Variables'''
# The Variable name must start with a </letter/> or the </underscore_/>
# A variable name cannot start with a </Number/>
# A variable name can only be included by alpha-numeric cheracters and a underscore.
# (A to Z, 0 to 9, and _ )
# Variable names are case-sensitive 
# Ex: Name, name, NAME are three differnt variables 
# Variable name should not be matched with the keywords

_message = "Hello World"
print(_message)

a10 = 20
print(a10)

a_10 = 30
print(a_10)

message = "Hello"
Message = "Welcome to"
MESSAGE = "Python"
MessAge = "Programming"
print(message, Message, MESSAGE, MessAge, sep = '\n')

'''Incorrect Variable Names'''
'''

01a = 20 #variable name start with a number

message*01 = "Hello World" #variable name cannot be included with a special character
print(message*01)

'''
