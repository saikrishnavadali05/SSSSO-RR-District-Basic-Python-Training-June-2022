#Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function
#solution
n=input("enter elements seperated by ,")
list1=n.split(',')
tuple1=tuple(list1)
new_list=tuple1[::2]
print("The alternative elements of a given tuple is",new_list)