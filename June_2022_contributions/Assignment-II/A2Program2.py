#2.Given a Full name stored in a input file input_name.txt which contains first name, middle name and last name. All the first, middle and last name are seperated by spaces. Print the output in the following order: Last Name, First Name, middle name. Next, Save the last name in last_name.txt file. Save the first name in first_name.txt. Save the middle name in middle_name.txt file.
with open(r"C:\Users\SRIKANTH\Desktop\fullname.txt", "r") as f:
    line = f.readline()
data = line.split()
print(data[-1], data[0], data[1])
with open(r"C:\Users\SRIKANTH\Desktop\last_name.txt", "w") as f:
    f.write(data[-1])
with open(r"C:\Users\SRIKANTH\Desktop\first_name.txt", "w") as f:
    f.write(data[0])
with open(r"C:\Users\SRIKANTH\Desktop\middle_name.txt", "w") as f:
    f.write(data[1])