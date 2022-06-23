from optparse import Values


Student_list = {
'Neeraj': '20, BA, Punjab',
'Arsh': '20, BCA, Punjab',
'Sakshi': '23, MA, Haryana',
}

#Retrieving values from keys
print(Student_list['Neeraj'])
print(Student_list['Arsh'])
print(Student_list['Sakshi'])
#Entire Dictionary
print(Student_list)

# Key value pair separately
for keys, values in Student_list.items():
    print(keys, values, sep = ":")

#Printing only values
for values in Student_list.values():
    print(values)