#17.Write a script to read first n lines of a file. Accept filename and n as input from the user. Similar to Unix head command. (understand how unix head command works by searching on google or youtube).
#solution 1
def file_read_from_head(file_name, nlines):
        from itertools import islice
        with open(file_name) as f:
                for line in islice(f, nlines):
                        print(line)
file_name=input("Enter the File Name : ")
nlines=int(input("Enter the number of lines to be read : "))
file_read_from_head(file_name,nlines)


#solution 2
def read_lastnlines(File_name,n):
	with open(File_name) as f:
		for line in (f.readlines() [:n]):
			print(line)
name_of_the_file = str(input("Enter the name of the file "))
File_name = name_of_the_file + ".txt"
Number = int(input("Enter the number of lines that needs to be printed "))
read_lastnlines(File_name,n)