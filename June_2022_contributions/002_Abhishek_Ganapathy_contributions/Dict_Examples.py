# Dict notation : {} (curly braces)
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Dictionary values can be accessed with the help of using corresponing keys in (square brackets) []
print(student['name'])

# Finding out the number of keys in dict can be done with the help of len() function
print(len(student))

# Print all the keys with keys() method 
for key in student.keys():
    print(key)

# Print all the values with values() method 
for value in student.values():
    print(value)

# Print both the keys as well as the values with items() method
for key, value in student.items():
    print(key, value)

user_dict = {
  "name": "Ganesh",
  "Age": 18,
  "Weight": 60,
  "Height": 5.8
}
employee = user_dict["name"]
print(employee)

print("--------------------------------------------------")
months = {'fourth_month': 'April', 'second_month': 'Feb', 'fifth_month': 'May', 'first_month': 'Jan'}
print(months)
print(months['fourth_month'])
months[3] = 'March'
print(months)
print("keys assigned in dictionary :", months.keys())
print("values assigned to keys :", months.values())
del months['second_month']
for key in months:
    print(key, months[key])
print(months.pop(3))
print(months)
print(5 in months)
print(3 in months)
print(months.get('first_month'))
# del months
months.clear()
print(months)

print("----------------------------------------------")

my_dict = {}
# Creating a Dictionary with Mixed keys
my_dict = {'Name': 'Multiple_wishes', 1: [1, 2]}
print(my_dict['Name'])
print(my_dict[1])
my_dict[1] = 5, 6
my_dict[2] = 2, 3, 4
print("\nDictionary with the use of Mixed Keys: ")
my_dict[3] = {'Nested': {1: 'Hyderabad', 2: 'Telangana'}}
print(my_dict)
print(my_dict[3]['Nested'][2])
# Creating a Dictionary with dict() method
my_dict = dict({1: 'Multiple_wishes', 2: 'Py_wishes', 3: 'Company'})
print("\nDictionary with the use of dict(): ")
print(my_dict)
# Creating a Dictionary with each item as a Pair
my_dict = dict([(1, 'Multiple_wishes'), (2, 'Hyderabad')])
print("\nDictionary with each item as a pair: ")
print(my_dict)
cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
for i in cubes:
    print(cubes[i])
print("Len = ", len(cubes))
print("\nby using range statement")
for i in range(1, 6):
    print(i ** 3)