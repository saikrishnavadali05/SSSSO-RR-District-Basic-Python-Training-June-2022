# Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.
a = 10
b = 3.14
c = "Prashanth"
d = True
print("int_type id is", id(a))
print("float_type id is", id(b))
print("string_type id is", id(c))
print("bool_type id is", id(d))
converted_list = [str(a), int(b), set(c), int(d)]
print(converted_list)