# Store student name, id, age, class, course in a dictionary. Write a script to lookup a student name, age, class, course given the student ids.

# Student Data Dictionary
students = {1:['Prashanth',18,12,'Python'], 2:['Vijay',17,11,'Java'], 3:['Ramesh',18,12,'C#']}

id = int(input("Enter student id: "))

data = students.get(id,-1)

if data == -1:
    print("No Student found!")
else:
    print('Name:', data[0])
    print('Age:', data[1])
    print('Class:', data[2])
    print('Course:', data[3])

