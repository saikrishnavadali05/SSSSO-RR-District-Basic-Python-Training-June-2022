# Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User

mylist = []
count = int(input('Enter the number of elements you need in a list: '))

for i in range(count):
    element = int(input('Enter an integer element of your choice for element: '))
    mylist.append(element)
print(mylist)
print('Largest in the list is:', max(mylist))
print('Smallest in the list is: ', min(mylist))

