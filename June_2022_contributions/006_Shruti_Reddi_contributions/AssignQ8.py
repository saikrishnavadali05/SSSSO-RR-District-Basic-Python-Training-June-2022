#Write a program to create variables storing values for each datatype. 
#print the object identities of all the created variables. 
#Next, convert the types of the each varible into another type. 
#After changing the type, store all the values of all the variables in a list. Finally, Print the list.

#There are 5 types of data in Python to declare a variable. 
 #Number Variable in Python   
 #Define Integer Variable
myInt = 18
print(myInt)

#Define Floating Point Variable
myFloat = 10.12
print(myFloat)

#List Variable in Python

myList = ['Ram', 'Shyam', 'Mahesh', 'Bilal', 'Ramesh', 'Ganesh']
print(myList)

#String Variable in Python
myString = 'This is my string.'
print(myString)

#Tuple Variable in Python
myTuple = ('Ram', 'Shyam', 'Mahesh', 'Bilal', 'Ramesh', 'Ganesh')
print(myTuple)

#Dictionary Variable in Python
myDict = {
	"one": "Ram",
	"two": "Shyam",
	"three": "Mahesh",
	"fore": "Bilal",
	"five": "Ramesh",
	"six": "Ganesh"
}
print(myDict)    
#Set Variable in Python

#declare Set in Python
mySet = {"Ram", "Shyam", "Mahesh", "Bilal", "Ramesh", "Ganesh"}
 
#Access elements of Set
for x in mySet:
	print(x)

c1=float(myInt)#convert to float
print(c1)

c2=int(myFloat)#convert to integer
print(c2)

c3=list(myString)#convert to string
print(c3)

c4=tuple(myString)#convert to tuple
print(c4)

c5=list(myTuple)
print(c5)

list_new=[c1, c2, c3, c4, c5]
print(list_new)