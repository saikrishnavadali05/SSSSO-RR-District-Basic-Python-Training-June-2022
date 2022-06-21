# 1.Write a program to print 
# each word of the line in a new line using both while and for loops.

string = input("Enter the string here: ")

word = string.split(' ')

for i in word:
    print(i)

