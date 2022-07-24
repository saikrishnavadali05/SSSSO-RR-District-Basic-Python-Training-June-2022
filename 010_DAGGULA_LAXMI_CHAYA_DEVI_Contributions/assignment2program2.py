# Given a Full name stored in a input file input_name.txt which contains first name,
# middle name and last name. All the first, middle and last name are seperated by spaces
# . Print the output in the following order: Last Name, First Name, middle name.
# Next, Save the last name in last_name.txt file. Save the first name in first_name.txt.
#  Save the middle name in middle_name.txt file.


# input text from input_name.txt file
with open("input_name.txt", "r") as f:
    line = f.readline()
# split line in to words and storing in list

data = line.split()
# printing lastname firstname middlename
print(data[-1], data[0], data[1])

# saving lastname in last_name.txt file
with open(" last_name.txt", "w") as f:
    f.write(data[-1])

# saving firstname in first_name.txt file
with open("first_name.txt", "w") as f:
    f.write(data[0])

# saving middlename in middle_name.txt file
with open("middle_name.txt", "w") as f:
    f.write(data[1])
