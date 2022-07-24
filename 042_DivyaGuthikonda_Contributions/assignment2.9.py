#Store student name, id, age, class, course in a dictionary.
# Write a script to lookup a student name, age, class, course given the student ids.
'''
students={"1":{"Name":"Divya","Age":20,"Class":12,"Course":'MPC'},
          "2":{"Name":"Sandhya","Age":20,"Class":12,"Course":'BiPC'},
          "3":{"Name":"Shilpa","Age":20,"Class":12,"Course":'CEC'},
          "4":{"Name":"Krithika","Age":20,"Class":12,"Course":'HEC'},
          "5":{"Name":"Rani","Age":20,"Class":12,"Course":'Ploytech'}}
n=input("Enter Student Id:")
std=students[n]
print(std)
#output
#Enter Student Id:2
#{'Name': 'Sandhya', 'Age': 20, 'Class': 12, 'Course': 'BiPC'}

'''
def Studentdetails():
    name,id_,age,class_,course = "Divya",1,20,12,"MPC"
    print("Name: {}\nId: {}\nAge: {}\nClass: {}\nCourse: {}".format(name,id_,age,class_,course))
    name,id_,age,class_,course = "Sandhya",2,20,12,"BiPC"
    print("Name: {}\nId: {}\nAge: {}\nClass: {}\nCourse: {}".format(name,id_,age,class_,course))
    name,id_,age,class_,course = "Shilpa",3,20,12,"CEC"
    print("Name: {}\nId: {}\nAge: {}\nClass: {}\nCourse: {}".format(name,id_,age,class_,course))
    name,id_,age,class_,course = "Krithika",4,20,12,"HEC"
    print("Name: {}\nId: {}\nAge: {}\nClass: {}\nCourse: {}".format(name,id_,age,class_,course))
Studentdetails()
#output
'''
Name: Divya
Id: 1
Age: 20
Class: 12
Course: MPC
Name: Sandhya
Id: 2
Age: 20
Class: 12
Course: BiPC
Name: Shilpa
Id: 3
Age: 20
Class: 12
Course: CEC
Name: Krithika
Id: 4
Age: 20
Class: 12
Course: HEC
'''