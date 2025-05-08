#create logic to print more than 10 patterns:
no_rows=4
for row in range(1,no_rows+1):
    for column in range(1,row+1):
        print("*",end=" ")
    print()       

#create reverse oder:
no_rows=int(input("enter the no_rows:"))
for row in range(no_rows+1,0,-1):
    for column in range(1,row+1):
        print("*",end=" ")
    print()   
no_rows=4

for r in range(1,no_rows+1):
    for column in range(1,r+1):
        print("*",end=" ")
        print()
no_rows=int (input("enter the no of row:"))
for row in range(1,no_rows+1):
    for column in range(1,row+1): 
        print("my friend is",end=" ")
        print("very good",end=" ")
        print()
for r in range(1,no_rows+1):
    for column in range(1,r+1):
        print("column",end=" ")
        print()
for r in range(1,no_rows+1):
    for column in range(1,r+1):        
        print("{0}{1}".format(column,r),end=" ")
        print()
for r in range(1,no_rows+1):
    for column in range(1,r+1):
        print("{0}{1}".format(r,column),end=" ")
    print()

for r in range(no_rows+1,0,-1):
    for r in range(1,r+1):
        print("*",end=" ")
    print()   


#COMMAND LINE ARGUMENTS(Argvs):INPUT FUNCTION
import sys
print(sys.argv)      #['cla.py', '1', '2', '3', '4', '5', '2', '10', '1', '3']
print(len(sys.argv)) #10
sum=0
for i in range(1,len(sys.argv)):
    sum+=int(len(sys.argv[i]))
print("result",sum)        #10

import sys
print(sys.argv)      #['cla.py', 'name', 'age', '1', '3', '4', 'name', 'age', '13', '14']
print(len(sys.argv)) #10
sum=0
for i in range(1,len(sys.argv[0])):
    sum+=int(len(sys.argv[i]))
print("result:",sum)  #21    
a=tuple(sys.argv)
print("enter list into tuple:",a)  #enter list into tuple: ('cla.py', 'name', 'age', '1', '3', '4', 'name', 'age', '13', '14')
b=set(sys.argv)
print("remove duplicate values:",b)#remove duplicate values: {'age', '1', '14', '13', 'cla.py', '3', '4', 'name'}

