# 8.Write a program to create variables storing values for each datatype. 
# print the object identities of all the created variables. 
# Next, convert the types of the each varible into another type. 
# After changing the type, store all the values of all the variables in a list. 
# Finally, Print the list.

# creating the variables 
a = 12
print(type(a))
b = 65.43
print(type(b))
c = 9090
print(type(c))

# Converting the types.
d = float(a)
print(type(d))
e = int(b)
print(type(e))
f = str(c)
print(type(f))

# Creating the empty list 
list_of_variables = []

list_of_variables.append(a)
list_of_variables.append(b)
list_of_variables.append(c)
list_of_variables.append(d)
list_of_variables.append(e)
list_of_variables.append(f)

print(list_of_variables)

