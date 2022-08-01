#18.Write a script to read last n lines of a file. Accept filename and n as input from the user. Similar to Unix tail command. (understand how unix tail command works by searching on google or youtube).
#solution 1
def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
file_name=input("Enter the File Name : ")
n=int(input("Enter the number of lines to be read : "))
LastNlines(file_name,n) 

#solution 2
def read_lastnlines(fname,n):
	with open(File_name) as f:
		for line in (f.readlines() [-n:]):
			print(line)
name_of_the_file = str(input("Enter the name of the file "))
File_name = name_of_the_file + ".txt"
Number = int(input("Enter the number of lines that needs to be printed "))
read_lastnlines(File_name,Number)