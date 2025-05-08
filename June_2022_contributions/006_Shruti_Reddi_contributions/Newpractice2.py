#Exercise 6: Write all content of a given file into a new file by 
# skipping line number 5
file = open('army.txt', 'r')

lines=file.readlines()

fp =open('newtextfile.txt', 'w')

start_point =0
for line in lines:
    if start_point==4:
        start_point=start_point+1
        continue
    else:
        fp.write(line)

    start_point+=1