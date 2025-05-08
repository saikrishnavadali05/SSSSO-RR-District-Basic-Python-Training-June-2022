# 5.Write a program to print all the details of a student 
# by storing all of his details in a dictionary 
# by retrieveing the values from keys. Next, Print the entire dictionary. 
# Next, print each and every key value pair seperately. 
# Next, print only values (Don't print keys).

dict_1 ={
    'student_name':'Ranjith',
    'student_roll_no': '17N21A0505',
    'student_address': 'Metpally',
    'student_number': 8179176017,
    'student_cgpa': 7.51
}
# by retrieving the values from keys in dictionary.
print(dict_1['student_name'])
print(dict_1['student_roll_no'])
print(dict_1['student_address']) 
print(dict_1['student_number'])
print(dict_1['student_cgpa'])

# printing the entire dictionary.
print(dict_1)

# printing the each and every key value separately.
for key,values in dict_1.items():
    print(key,values,sep=':',end = "\n")

# printing the only values 

for i in dict_1.values():
    print(i)

