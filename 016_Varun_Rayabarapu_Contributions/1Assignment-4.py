#Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
a=tuple(map(int,input("enter elements with space : ").split()))
print("alternate elements of tuple are : ",a[0::2])
