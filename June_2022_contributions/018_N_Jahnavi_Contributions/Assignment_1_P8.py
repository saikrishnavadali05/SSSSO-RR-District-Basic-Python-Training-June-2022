# Program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.

place = "Hyderabad"
code = 500032
street = 22/7

print(type(place))
print(type(code))
print(type(street))

place = list(place)
code = float(code)
street = int(street)

Details = [place, code, street]

print("The list is : ", Details)
