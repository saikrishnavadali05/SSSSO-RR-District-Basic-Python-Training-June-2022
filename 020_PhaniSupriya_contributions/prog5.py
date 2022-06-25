#prog5
#Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
dict={'name':'Phani','rollnum':'30','class':'6','School':'Kendriya Vidyalay','gender':'female',}

for key in dict:
    print(key,':',dict.get(key))
print(dict)
for pair in dict.items():
    print(pair)
for value in dict.values():
    print("value:",value)