# Given a name which contains first and last name, 
# print the output in the following order: Last Name,First Name
# First_name = input("Enter Your First Name")
# Last_name = input("Enter Your Last Name ")
# 
# print(First_name,Last_name)
# print(Last_name,First_name)

Name = input("Enter the name First and Last Name here itself:")

name = Name.split(" ")

print(name[1],name[0])

