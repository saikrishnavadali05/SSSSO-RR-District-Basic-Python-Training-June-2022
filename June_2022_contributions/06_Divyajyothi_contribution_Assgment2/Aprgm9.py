#9.Store student name, id, age, class, course in a dictionary. Write a script to lookup a student name, age, class, course given the student ids.
student_details = {"name": "divyajyothi", "id": 456,
                   "age": 23, "course": "Bachloredegree", "branch": "ECE"}
id_no = int(input("Enter id:"))
if student_details["id"] == id_no:
    print("Name:", student_details["name"])
    print("Age:", student_details["age"])
    print("Class:", student_details["class"])
    print("Course:", student_details["course"])
else:
    print("Entered id is not present in the data,please enter valid id no THANK YOU ")