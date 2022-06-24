'''
5.	Write a program to print all the details of a student
by storing all of his details in a dictionary by retrieving
the values from keys. Next, print the entire dictionary.
Next, print each and every key value pair separately.
Next, print only values (Don't print keys).

'''
# Creating dictionary
students_data = {"Meena" : [55,88,77,66,44],
             "Umesh":[56,78,55,88,70],
             "Sushil": [44,65,76,33,77]}

# searching item in dictionary
name = input("Enter name of student :")
if name in students_data.keys():
    print("Details of the student:",students_data[name])
else :
    print("No student found")       

print()
print("Entire Dictionary : ")
print(students_data)
print()


# Prints key, value pairs separately
print("Key, Value Pairs:")
n=2
for index, (key, value) in enumerate(students_data.items()):
    while index <= n:
        print(key, '::', value)
        break

print()
print("Value Only:")
# Prints only values and not keys
n=2
for index, (key, value) in enumerate(students_data.items()):
    while index <= n:
        print(value)
        break