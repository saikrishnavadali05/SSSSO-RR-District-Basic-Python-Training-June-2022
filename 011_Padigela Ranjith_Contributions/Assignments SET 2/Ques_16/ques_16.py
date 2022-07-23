"""
16.Create a function display_student_data() which takes student id, 
student name and marks as input. It should display all the data. 
If marks is missing it should display 75.
"""
def display_student_data(id,name,marks=75):
    return id,name,marks
print(display_student_data(1,'Ranjith',34))
print(display_student_data(2,'ajith'))