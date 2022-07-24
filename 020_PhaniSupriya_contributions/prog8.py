#prog8
#Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.

a = "9"
b = 404
c = 10.4
d = 3 + 4j
e = 30
print("Object Identity of variable a is:", id(a))
print("Object Identity of variable b is:", id(b))
print("Object Identity of variable c is:", id(c))
print("Object Identity of variable d is:", id(d))
print("Object Identity of variable e is:", id(e))
P = int(a)
Q = complex(b)
R = str(c)
S = float(e)
List = [P,Q,R,S]
print(List)