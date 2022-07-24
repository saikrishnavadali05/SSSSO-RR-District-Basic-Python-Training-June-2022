Flag = False
Student_Dictionary = {
    'Name1':'Abhishek',
    'Age1':32,
    'Class1':"12th",
    'Course1':'MBA'
}

Search = str(input("What do you want to search? "))
for values in Student_Dictionary:
    if (Student_Dictionary.get(Search)):
       Flag = True 
    else:
        Flag = False
if (Flag == True):
    print("The string is not found")
else:
    print("The string is found")