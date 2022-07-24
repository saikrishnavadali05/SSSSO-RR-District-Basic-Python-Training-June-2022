file = open('geek.txt','w')
file.write("This is the write command")
file.write("\nIt allows us to write in a particular file")
file.close()

# Python code to illustrate append() mode
file = open('geek.txt','a')
file.write("\nThis will add this line")
file.close()

# Python code to illustrate split() function
with open("geek.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = len(line)
        print (word)
file.close()