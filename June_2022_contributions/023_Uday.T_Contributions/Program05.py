#Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
#solution
student_details={"Name":"T Uday","Gender":"MALE","Studying":"BTech","Branch":"ECE","RollNo":"09"}
#printing Entire dictionary
print(student_details)
#printing each key value pair seperately
for key,value in student_details.items():
    print(key,":",value)
#printing only values
for key,value in student_details.items():
    print(value)