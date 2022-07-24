#Creating dictionary
student_data = {"Name":'Sahithi',"Rollno":123,"Class":'Msc',"Phy_marks":50,"Maths_marks":60,"Che_marks":70,"toatal_Avg":60}
print("The given dictionary is :")
print(student_data)
print()
for item in student_data:
    print("key : {} , value : {}".format(item,student_data[item]))
for item in student_data:
    print(student_data[item])    

