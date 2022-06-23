student_data = {"Name":'Sai',"Rollno":4569,"Class":'mca',"com_marks":90,"Maths_marks":80,"eng_marks":70,"toatal_Avg":80}
print("The given dictionary is :")
print(student_data)
print()
for item in student_data:
    print("key : {} , value : {}".format(item,student_data[item]))
for item in student_data:
    print(student_data[item])