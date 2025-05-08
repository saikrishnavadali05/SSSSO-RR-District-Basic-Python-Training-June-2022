#problem statement:to print each word of the line in a new line using both while and for loops
string="Love All Serve All Help Ever Hurt Never"
#method1
for i in string:
    print(i,end='')
    if(i==" "):
        print()
#method2
list1=string.split(' ')
for i in list1:
    print(i)
    