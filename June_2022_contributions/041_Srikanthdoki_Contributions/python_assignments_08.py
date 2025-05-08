# problem statement:Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list.
a = int(input("Enter a integer value for a: "))
b = float(input("Enter a float value for b: "))
c = input("Enter a value for c: ")
print(a, b, c)
print(type(a))
print(type(b))
print(type(c))
List = []
List.append(a)
List.append(b)
List.append(c)
print(List)