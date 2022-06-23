# Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. 
# Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).


# Number_of_Entry = int(input("Enter the number of Students whose details to be entered "))
# for i in range(0,Number_of_Entry):
#     Student_details = dict(input("Enter key and value ").split())
# Length = len(Student_details)
Student_details = {
    "Name1":"Abhishek", 
    "Age1":32,
    "Weight1":75,
    "Height1":5.11,
    "Name2":"Ashok",
    "Age2":30,
    "Weight2":85,
    "Height2":6.11,
    "Name3":"Francis",
    "Age3":35,
    "Weight3":105,
    "Height3":5.00
}
Length = len(Student_details)
print("The length of the dictionary is",Length)
print("Print Entire Dictionary")
print(Student_details)
print("Print each and every key value pair seperately")
for key in Student_details:
    print(key, Student_details[key])
print("Print only values (Don't print keys)")
for key in Student_details:
    print(Student_details[key])
print("Enter the key value for which you want the value")
Key_Number = (input("Enter the number "))
print(Student_details[Key_Number])


