myDict = {
'Nageshwari': 'Female, 19, BTech, Nizamabad',
'Sachin': 'Male, 23, Working, Hyderabad',
'Ruchitha': 'Female, 20, Degree, Armoor',
'Pranitha': 'Female, 20, BTech, Khammam',
'Prathima': 'Female, 20, BTech, Hyderabad',
}

# details in a dictionary by retrieveing the values from keys
print(myDict['Nageshwari'])
print(myDict['Sachin'])
print(myDict['Ruchitha'])
print(myDict['Pranitha'])
print(myDict['Prathima'])

# Entire Dictionary
print(myDict)

# Key Value Pair Seperately
for keys, values in myDict.items():
    print(keys, values, sep = ": ")

# Printing only Values 
for values in myDict.values():
    print(values)






