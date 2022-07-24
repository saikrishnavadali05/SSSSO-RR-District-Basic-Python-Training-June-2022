#problem statement:Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values
dict1={'name':'supriya','rollno':'50','gender':'female'}
for key in dict1:
    print(key,':',dict1.get(key))
print(dict1)
for i in sorted(dict1.items()):
    print(i)
for key in dict1:
    print('value',dict1.get(key))