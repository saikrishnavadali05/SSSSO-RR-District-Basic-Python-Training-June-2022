#Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.
a=10
print("data type of a is",type(a))
b=10.50
print("data type of b is",type(b))
c="11"
print("data type of c is",type(c))
a=str(a)
b=int(b)
c=float(c)
print("after converting and making list -",[a,b,c])
