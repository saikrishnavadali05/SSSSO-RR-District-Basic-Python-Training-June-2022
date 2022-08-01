#Question5: Write a program to print all the details of a student by storing all of his details
# in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. 
# Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
Student_Details={"Name":"G Rajasekhar","Gender":"Male","Studying":"MTech","Branch":"DECS","RollNo":"435"}

print(Student_Details)
#printing each key value pair seperately
for key,value in Student_Details.items():
    print(key,":",value)
#printing only values
for key,value in Student_Details.items():
    print(value)