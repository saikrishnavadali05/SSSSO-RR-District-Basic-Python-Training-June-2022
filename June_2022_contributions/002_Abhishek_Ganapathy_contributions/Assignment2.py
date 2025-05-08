# Enter First Name and Last Name and then Print the output
F_Name = (input("Enter First Name "))
L_Name = (input("Enter Last Name "))
print("The name entered is",F_Name,L_Name)
print("Hello", L_Name,F_Name)

# Enter the full name and then split according to space
Full_Name = (input("Enter Full Name "))
First_Name = Full_Name.split()[0]
Last_Name = Full_Name.split()[-1]
print("First Name", First_Name)
print("Last_Name", Last_Name)

