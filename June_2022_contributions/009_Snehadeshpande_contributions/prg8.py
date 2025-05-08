'''problem statement:Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list.
 Finally, Print the list.'''
a=1
b=float(a)
c=2.75
d=int(c)
e=1232
f=str(e)
list1=[]
list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)
list1.append(e)
list1.append(f)
print(list1)