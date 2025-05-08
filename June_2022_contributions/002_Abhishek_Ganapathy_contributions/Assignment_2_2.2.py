res = str
File_input = open("Assignment_2_2.2_Input.txt","r")
for i in File_input:
    res = i, res
    print(res)
File_input_1 = open("Assignment_2_2.2_Input.txt")
content = File_input_1.readlines()
print("Last Name", content[2])
print("First Name", content[0])
print("Middle Name", content[1])

File_input_2 = open("Assignment_2_2.2_FirstNameOutput.txt","w")
File_input_3 = open("Assignment_2_2.2_MiddleNameOutput.txt","w")
File_input_4 = open("Assignment_2_2.2_LastNameOutput.txt","w")
File_input_2.write(content[0])
File_input_3.write(content[1])
File_input_4.write(content[2])
File_input.close()
