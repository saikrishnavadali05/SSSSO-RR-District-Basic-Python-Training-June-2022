"""
Given a Full name stored in a input file input_name.txt 
which contains first name, middle name and last name. 
All the first, middle and last name are seperated by spaces. 
Print the output in the following order: Last Name, First Name, middle name. 
Next, Save the last name in last_name.txt file. Save the first name in first_name.txt. 
Save the middle name in middle_name.txt file.
"""
Full_name = open("input_name.txt","r")
x = Full_name.readline()
lst = x.split()

first_name = open("first_name","w")
first_name.write(lst[0])

middle_name = open("middle_name.txt","w")
middle_name.write(lst[1])

last_name = open("last_name.txt","w")
last_name.write(lst[2])