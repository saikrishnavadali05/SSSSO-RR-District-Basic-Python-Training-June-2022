#Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys.
# Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).

#Dict notation : {} (curly braces)
student = {'name': 'Shruti', 'age': 30, 'Education': 'B.Tech','Specialization':'Chemical'}

# Dictionary values can be accessed with the help of using corresponing keys in (square brackets) []
#print(student['name'])
#print(student['age'])
#print(student['Education'])
#print(student['Specialization'])

# Finding out the number of keys in dict can be done with the help of len() function
#print(len(student))

# Print all the keys with keys() method 
#for key in student.keys():
    #print(key)

#Print all the values with values() method 
#for value in student.values():
    #print(value)

# Print both the keys as well as the values with items() method
for key, value in student.items():
    print(key, value)