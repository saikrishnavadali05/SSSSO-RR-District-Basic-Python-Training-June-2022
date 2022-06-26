# Write the script of the student form(name_of_student, class_studying, 
# college_name, city_lives) that accepts as command line parameters and prints as

from sys import argv

stdt_nm = argv[1]
cls = argv[2]
Clg_nm = argv[3]
City = argv[4]

print("Student Name : ",stdt_nm)
print("Class        : ",cls)
print("College_Name : ",Clg_nm)
print("City_lives   : ",City)
