#problem statement:Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
n=input("enter elements seperated by ,")
list1=n.split(',')
tuple1=tuple(list1)
for i in range(0,len(tuple1),2):
    print(tuple1[i])