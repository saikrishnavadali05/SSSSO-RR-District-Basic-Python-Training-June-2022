def read_lastnlines(fname,n):
	with open(File_name) as f:
		for line in (f.readlines() [-n:]):
			print(line)
name_of_the_file = str(input("Enter the name of the file "))
File_name = name_of_the_file + ".txt"
Number = int(input("Enter the number of lines that needs to be printed "))
read_lastnlines(File_name,Number)