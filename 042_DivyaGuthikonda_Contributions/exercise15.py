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
file=open("demo.txt","w")
file.write("\n 6. This line is uploaded to the existing file")
file.close()
#(to know whether the content is uploaded or not)
file=open("demo.txt", "r")
print(file.read())
# output
'''
1. Steve Jobs is a popular name in the world.
2. He was the co-founder and chairman of Apple Inc.
3. He is also referred to as an industrial designer, investor, and media tycoon.
4. His full name was Steven Paul Jobs.
5. He was born on 24th February in the year 1955.
 6. This line is uploaded to the existing file
'''


#Write a script that append lines to the file that are created in problem 3 and they are
file=open("demo.txt", "a")
Lines=["\n1. Steve Paul Jobs is regarded as a successful American businessman.",
"\n2. He had attained success in different fields.",
"\n3. He had a great contribution to the development of computers and mobiles.",
"\n4. He is stated as the initiator of the personal computer revolution.",
"\n5. He had served as the CEO of Apple Inc from 1997 to 2011."]

file=open("demo.txt", "r")
print(file.read())
#These lines were appeded in a demo.txt file
#multiple lines can't be add 
#to add multiple lines the content must be write in a list
'''
1. Steve Paul Jobs is regarded as a successful American businessman.
2. He had attained success in different fields.
3. He had a great contribution to the development of computers and mobiles.
4. He is stated as the initiator of the personal computer revolution.
5. He had served as the CEO of Apple Inc from 1997 to 2011.
'''
