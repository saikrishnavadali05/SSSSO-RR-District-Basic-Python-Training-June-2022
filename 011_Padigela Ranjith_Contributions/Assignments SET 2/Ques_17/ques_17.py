"""
17.Write a script to read first n lines of a file. Accept filename 
and n as input from the user. Similar to Unix head command. 
(understand how unix head command works by searching on google or youtube).
"""



N = int(input("Enter the number here: "))

f = open('Myfile_data.txt')

head = [next(f) for i in range(N)]
print(head)

f.close()