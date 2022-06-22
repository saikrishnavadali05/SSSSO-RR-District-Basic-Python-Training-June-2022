#Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
di={"Name":'Varuntej',"Section":"A","Roll.no":"44","Marks":100}
for key in di:
    print(key,':',di.get(key))
print(di)
for i in sorted(di.items()):
    print(i)

print(di.values())
