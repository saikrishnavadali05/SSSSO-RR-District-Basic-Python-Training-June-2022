#What is zen of python? 
#  Answer:
# The Zen of Python is a collection of 19 "guiding principles" for writing computer programs \n
#  that influence the design of the Python programming language.

#Write a program to illustrate "zen of python"?
a=5
print("id(a) =",id(a))
b=a+2
print("id(b) =",id(b))
a=a+3
print("id(a) =",id(a))
print("a value is: ",a)

#output
'''
id(a) = 140708864775328
id(b) = 140708864775392
id(a) = 140708864775424
a value is:  8
'''