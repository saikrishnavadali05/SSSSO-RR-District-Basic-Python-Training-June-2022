"""
Store student name, id, age, class, course in a dictionary. 
Write a script to lookup a student name, age, class, course given the student ids.
"""

student_details = [{"Name":"Ranjith","id":101,"class":"B.tech","age":22,"course":"Python"},
                   {"Name":"Rohith","id":102,"class":"Bsc","age":21,"course":"java"},
                    {"Name":"Raju","id":103,"class":"ssc","age":18,"course":"IIT"},
                    {"Name":"Ramesh","id":104,"class":"B.Com","age":23,"course":"Power BI"},
                    {"Name":"Lokesh","id":105,"class":"CEC","age":20,"course":"Tableu"},]
student_id = int(input("Enter the student id here:"))

for i in range(len(student_details)):
    if student_details[i]['id'] == student_id:
        print("Name :",student_details[i]['Name'])
        print("Class :",student_details[i]['class'])
        print("Age :",student_details[i]['age'])
        print("course :",student_details[i]['course'])



