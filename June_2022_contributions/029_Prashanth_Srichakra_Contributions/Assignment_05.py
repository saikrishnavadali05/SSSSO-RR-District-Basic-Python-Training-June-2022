# Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).

student = {"name":"Prashanth", "marks":447, "age":18}
#Printing all the details of the student
print("Name of the student:", student["name"])
print("Age of the student:", student["age"])
print("Marks obtained by the student:", student["marks"])

# Printing the entire dictionary
print(student)

# Printing all the key:value pairs of the dictionary
for k, v in student.items():
    print(k,v,sep=":")

# Printing all the values(only) of the dictionary
for i in student.values():
    print(i, end=" ")