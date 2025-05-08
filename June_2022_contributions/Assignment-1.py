
# 1) Write a program to print each word of the line in a new line using both while and for loops.
#Input : Love All Serve All Help Ever Hurt Never
str = ("Love","All","Serve","All","Help","Ever","Hurt","Never")
for i in str:
     print(i)
#Output : 
#Love
#All
#Serve 
#All 
#Help
#Ever
#Hurt
#Never

# 2)Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)

a = 23
b = 34
print(max(a,b))     #34
print(min(a,b))     #23  int(argv)
print(a*b)          #782
print(a+b)          # 57
average = a+b/2
print("average of two numbers=",average) #average of two numbers= 40.0

#3)Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)

from sys import argv
print ("argvlist:", argv)
#argvlist: ['Assignment-1.py', '2', '3', '4', '5', '6']
X = ['Assignment-1.py','2','3','4','5','6']
Y = X[::-1]
print(Y)
#['6', '5', '4', '3', '2', 'Assignment-1.py']

#4)Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.

t = eval(input("Enter input for tuple:"))
t1 = ()
t2 = ()
i = 0
while i < len(t):
     if % 2 == 0:
        t1 += (t[i],)
     else:
        t2 += (t[i],)
     i += 1
#print("Alternative elements")
#print(t1)
#print(t2)

#Enter input for tuple:(0,2,4,5,6,7,8)
#Alternative elements
#t1=(0, 4, 6, 8)
#t2=(2, 5, 7)    


# 5) Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).

person = {'name': 'John', 'age': 25, 'group':'B.sc'}
print(person)
#{'name': 'John', 'age': 25, 'group': 'B.sc'}
for key, value in person.items():
    print(key, value)
#name John
#age 25
#group B.sc
print(person.values())
#dict_values(['John', 25, 'B.sc'])


#6.Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

from sys import argv
print("argvlist:",argv)

p = int(argv[1])
x = int(argv[2])
y = int(argv[3])
z = int(argv[4])
# argvlist: ['Assignment-1.py', '3', '4', '4', '5']
list = [3,4,4,5]
list.append(6) # [3,4,4,5,6]
#list = tuple(list)
#print(list)
#(3,4,4,5)
print(list)

#7)Write a program to print this pattern (hint : use \t and \n wherever required).
print("\t\t*\t\t\n\t* python *\t\n\t * is * a\t*\n\t* good * programming * language *\n* to * learn * for * beginners *")
#         *
#     * python *
#   * is  *  a    *
# * good  * programming * language *
#* to * learn * for * beginners *



#8)Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.

a=4
b=3.4
c=2+3j

m=type(a)
print(m)  # <class 'int'>
n=type(b)
print(b)    #3.4
3.4
o=type(c)
print(o)   #<class 'complex'>
x = float(a) #convert from int to float
y = complex(a) #convert from int to complex
z= int(b) #convert from float to int:
p = complex(b) #convert from float to complex

#output
#4.0
#(4+0j)
#3
#(3.4+0j)

print(x)
print(y)
print(z)
print(p)

list = [a,b,c]
print(list)
#[4, 3.4, (2+3j)]




# 9)write a program that imports numpy, matplotlib, pandas libraries. If the program imports those modules successfully. print "modules imported successfully" (hint : research about these libraries in google. Find out the command of how to install those libraries. Understand the purpose and importance of these libraries).

import numpy as np
import pandas as pd
import matplotlib as plt
print("modules import successfully")

# out put
# modules import successfully


# 10) What is zen of python? Write a program to illustrate "zen of python"? (Hint : Search on google.)
The Zen of Python is a collection of 19 "guiding principles" for writing computer programs

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
