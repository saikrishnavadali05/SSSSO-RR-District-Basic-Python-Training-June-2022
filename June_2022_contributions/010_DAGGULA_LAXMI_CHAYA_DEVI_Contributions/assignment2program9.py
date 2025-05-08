# defining dictionary
student_details = {"name": "chaya", "id": 513,
                   "age": 20, "class": "btech3rd year", "course": "cse"}
idno = int(input("Enter id:"))
if student_details["id"] == idno:
    print("Name:", student_details["name"])
    print("Age:", student_details["age"])
    print("Class:", student_details["class"])
    print("Course:", student_details["course"])
