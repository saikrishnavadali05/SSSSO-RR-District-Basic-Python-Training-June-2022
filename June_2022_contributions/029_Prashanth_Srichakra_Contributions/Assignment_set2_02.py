# Given a Full name stored in a input file input_name.txt which contains first name, middle name and last name. All the first, middle and last name are seperated by spaces. Print the output in the following order: Last Name, First Name, middle name. Next, Save the last name in last_name.txt file. Save the first name in first_name.txt. Save the middle name in middle_name.txt file.

# Reading name from input_name.txt
with open("input_name.txt", 'r') as f:
    input_name = f.read()
    split_name = input_name.split(" ")
    fname = split_name[0]
    mname = split_name[1]
    lname = split_name[2]

# Printing name in Last_name, First_name, Middle_name Format
print(lname,fname,mname)

# Writing lname into last_name.txt
with open("last_name.txt", 'w') as f:
    f.write(lname)

# Writing fname into first_name.txt
with open("first_name.txt", 'w') as f:
    f.write(fname)

# Writing mname into middle_name.txt
with open("middle_name.txt", 'w') as f:
    f.write(mname)


# File Contents

# input_name.txt
# Sachin Ramesh Tendulkar

# first_name.txt
# Sachin

# middle_name.txt
# Ramesh

# last_name.txt
# Tendulkar