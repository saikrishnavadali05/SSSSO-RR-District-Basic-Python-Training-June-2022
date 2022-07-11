#Store student name, id, age, class, course in a dictionary.
#  Write a script to lookup a student name, age, class,
#  course given the student ids.

from ast import Str


def student_info(student_id,student_name,student_age,student_class,student_course):
   student_dic = dict()
   student_dic[student_id] = [student_name,student_age,student_class,student_course]
   return student_dic
while True:
 s = input("Enter 'n' if you want to add a new student,enter 'any key 'if you want to finish: ")
 if s == 'n':
        ID = input("Student ID: ")
        name = input("Student name: ")
        age = input("Student Age: ")
        sclass=input("Student Class: ")
        course=input("Student COurse:")

        print(student_info(ID,name,age,sclass,course))
 else:
    break