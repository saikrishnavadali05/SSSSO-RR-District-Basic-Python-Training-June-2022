#Write a script that count the number of lines in a file. Take any file you wish
file=open("demo.txt","r")
count=0
Text=file.read()
Lines=Text.split("\n")
for i in Lines:
    if i:
        count+=1
print("The Number of lines in the file :",count)
#The Number of lines in the file : 5

#  Write a script that write lines to the file and they are