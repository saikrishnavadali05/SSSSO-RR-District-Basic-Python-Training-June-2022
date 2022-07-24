#Assignments (SET - 1)
#1.Write a program to print each word of the line in a new line using both while and for loops.
#Input : Love All Serve All Help Ever Hurt Never
from sys import argv
argv="Love","All","Serve","All","Help","Ever","Hurt","Never"
for i in argv:
    print(i)    #Love  All  Serve  All  Help  Ever  Hurt  Never
#2.Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)
a=23
b=34
c=(a,b)
maximum=max(c)
print("maximum is :",maximum)                 #maximum is : 34
minimum=min(c)
print("minimum is :",minimum)                 #minimum is : 23
addition=sum(c)
print("addition is :",addition)               #addition is : 57
d=addition/2
print("averege is :",d)                       #averege is : 28.5
multiplication=a*b
print("multiplication is :",multiplication)   #multiplication is : 782     

#3.Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)
L=["command","line","19","Argv"]
m=L[::-1]
print("enter the reverse order",m)    #enter the reverse order ['Argv', '19', 'line', 'command']
#create command line arguments:
from sys import argv
argv=["python","set.py",61,52,89,1]
print(type(argv))                     #<class 'list'>
print(len(argv))                      #6
print(argv)                           #['python', 'set.py', 61, 52, 89, 1]
a=["python_setpy","15","30","65"]
for a in argv:
  print(a)              #python   #set.py  #61  #52  #89  #1     

#4.Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
T=eval(input("enter input for tuple:"))     #(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
T1=()
T2=()
for i in range(len(T)):
  if i%2==0:
    T1+=(T[i],)
  else:
    T2+=(T[i],)
  i+=1
print("Alternative eliments:")   #Alternative eliments:
print(T1)                        #(0, 2, 4, 6, 8, 10, 12, 14)
print(T2)                        #(1, 3, 5, 7, 9, 11, 13, 15)  

#5.Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
student_datails={"name":"Ramu","age":"20","group":"b.come","gender":"male","address":"palamaner"}
dic=student_datails
print(dic.keys())       #dict_keys(['name', 'age', 'group', 'gender', 'address'])
print(dic)
print(dic.items())      #dict_items([('name', 'Ramu'), ('age', '20'), ('group', 'b.come'), ('gender', 'male'), ('address', 'palamaner')])
print(dic.values())     #dict_values(['Ramu', '20', 'b.come', 'male', 'palamaner'])  '''  

#6.Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.
import sys
print(sys.argv)        #['set.py', '1', '3', '4', '3', '2', 'mahi', 'naga']
print(len(sys.argv))    #8
sum=0
for i in range(1,len(sys.argv)):
  sum+=int(len(sys.argv[i]))
print("result-",sum)        #result- 13
  
a=tuple(sys.argv)
print("change list into tuple:",a) #change list into tuple: ('set.py', '1', '3', '4', '3', '2', 'mahi', 'naga')
b=set(sys.argv)
print("remove duplicates:",b)        #remove duplicates: {'4', '2', 'mahi', '1', 'naga', 'set.py', '3'}
from sys import argv
add=a
add=argv[1]+argv[2]+argv[3]+argv[4]+argv[5]
print("addition:",add)                 #addition: 12345

#7.Write a program to print this pattern (hint : use \t and \n wherever required)
print("\t"," ","*")
print("       ","*","python","*")
print("     ","*","is","*"," ","a"," ","\t","*")
print("   ","*","good","*","programming","*","language","*")
print("*","to","*","learn","*","for","*","beginners","*")  
#           *
#        * python *
#      * is *   a         *
#    * good * programming * language *
#* to * learn * for * beginners *  

#8.Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.
all_var=(13,"20.9","3+2b","true","mahi")
print(type(all_var))                     #<class 'tuple'>
a=list(all_var)
print("a is:",a,"\n","type(a):",type(a))   #a is:[13, '20.9', '3+2b', 'true', 'mahi']  ,#type(a): <class 'list'>
l=a
l=bool(a[0])
print(l)     #True  
s={"name","age","address"}
b=list(s)
print("b is:",b,"\n","type(b):",type(b)) 
var={"name":'naga',"age":'23',"address":'palamaner',"gender":'female'}
print("var of keys:",var.keys(),"\n","var of values:",var.values(),"\n","var of items:",var.items())  
#output:
#var of keys: dict_keys(['name', 'age', 'address', 'gender']) 
# var of values: dict_values(['naga', '23', 'palamaner', 'female']) 
# var of items: dict_items([('name', 'naga'), ('age', '23'), ('address', 'palamaner'), ('gender', 'female')])
print(type(var))         #<class 'dict'>
print(var.items())              #<class 'dict_items'>  
#9.Write a program that imports numpy, matplotlib, pandas libraries. If the program imports those modules successfully. print "modules imported successfully" (hint : research about these libraries in google. Find out the command of how to install those libraries. Understand the purpose and importance of these libraries).
numpy import as np
pandas import as pd
matplotlib import as plt
print("modules successfully")
#10.What is zen of python? Write a program to illustrate "zen of python"? (Hint : Search on google.)
output:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!   
Very IMPORTANT! Please search in google whenever you are stuck. Even if you get an error (traceback). Search about that traceback on google. For every difficulty or uncertainity, don't forget to search on google.
