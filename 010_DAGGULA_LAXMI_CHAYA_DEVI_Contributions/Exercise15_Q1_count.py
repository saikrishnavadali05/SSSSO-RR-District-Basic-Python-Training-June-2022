# count number of lines in a file
# opening file in read mode
# using readlines.readlines() function returns the list of all items in file (suggested for small files)
with open("Lines.txt", "r") as f:
    count = len(f.readlines())
print("Number of lines in Lines.txt:", count)
# better method for large files (enumerate useful for efficient memory storage)
with open("Lines.txt", "r") as f:
    count1 = 0
    for lines in enumerate(f):
        count1 += 1
print("Number of lines in Lines.txt(method2):", count1)
