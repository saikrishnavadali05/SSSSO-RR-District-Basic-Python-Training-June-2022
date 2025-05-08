#Given a Full name stored in a input file input_name.txt
#  which contains first name, middle name and last name.
#  All the first, middle and last name are 
# seperated by spaces. Print the output in the following order: 
# Last Name, First Name, middle name. 
# Next, Save the last name in last_name.txt file. 
# Save the first name in first_name.txt. 
# Save the middle name in middle_name.txt file.

 
file = open("input1_txt.txt", "r")
print(file.read())

file =open("lastname.txt", "w")
file.write("Lastname : Reddi")

file.close()

file =open("Middlename.txt", "w")
file.write("Middlename : Vasudevan")

file.close()

file =open("Firstname.txt", "w")
file.write("Firstname : Shruti")

file.close()
