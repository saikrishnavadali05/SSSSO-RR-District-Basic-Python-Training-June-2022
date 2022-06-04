"""
How to read specific lines from a File in Python?

"""

#solution

# open the sample file used
file = open('2.txt')

# read the content of the file opened
content = file.readlines()

# read 10th line from the file
print("fourth line")
print(content[4])

# print first 3 lines of file
print("first three lines")
print(content[0:3])
