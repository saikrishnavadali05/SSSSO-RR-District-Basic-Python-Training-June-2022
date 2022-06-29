# Given a list of numbers, write a Python program to find the sum of all the elements in the list.
mylist = input('Enter the integer elements of your choice seperated with a space: ').split()
print(mylist)

sum = 0
for elements in mylist:
    sum = sum + int(elements)
print('sum of the list is: ',sum)

