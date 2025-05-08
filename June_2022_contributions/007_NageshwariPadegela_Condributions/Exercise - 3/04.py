# Write the script of the student form(name_of_student, class_studying, college_name, city_lives) that accepts as command line parameters and prints as
'''
 student_name : Hareesh sai
 class        : 12th
 college_name : SSB
 city_lives   : Hyderabad
Here student_name value has spaces so keep in quotations to print the whole value.
'''
from sys import argv
student_name = argv[1]
Class = argv[2]
college_name = argv[3]
city_lives = argv[4]
print("Name of the student is",student_name, "he/she is studing in class", Class, "in", college_name, "college", "lives in ", city_lives)


