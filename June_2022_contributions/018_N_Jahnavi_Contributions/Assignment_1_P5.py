#  program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys.
#  Next, Print the entire dictionary. Next, print each and every key value pair seperately.
#  Next, print only values (Don't print keys).
print("\t")
Details_Of_Student = {'Name': 'Jahnavi', 'Age': 23, 'Degree' : 'MBA' }
print("The Dictionary of Student Details :", Details_Of_Student)

print("\t")
print(" The Items in the dictionary; key : value pair are as follows \n")
for key, value in Details_Of_Student.items():
    print(key, value)

print("\t")
print("Only Values of the dictionary are : ")
for value in Details_Of_Student.values():
    print(value)
