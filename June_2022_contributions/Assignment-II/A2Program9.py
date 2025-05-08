#9.Store student name, id, age, class, course in a dictionary. Write a script to lookup a student name, age, class, course given the student ids.
student_details = {"name": "srikanth", "id": 786,
                   "age": 32, "course": "MCA"}
id_no = int(input("Enter id:"))
if student_details["id"] == id_no:
    print("Name:", student_details["name"])
    print("Age:", student_details["age"])
    print("Course:", student_details["course"])
else:
    print("Entered id is not present in the data,please enter valid id no THANK YOU ")