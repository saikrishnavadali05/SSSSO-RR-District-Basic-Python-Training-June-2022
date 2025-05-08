myfile = open("test.txt", 'a')
myfile.write("\nI like to Code")
myfile.close()

myfile = open("test.txt", 'r')
read_lines = myfile.readlines()
myfile.close()

for line in read_lines:
    print(line, end="")
