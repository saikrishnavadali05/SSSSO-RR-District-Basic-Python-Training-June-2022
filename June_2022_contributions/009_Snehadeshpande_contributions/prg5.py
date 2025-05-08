dict1={'name':'sona','rollno':'01','gender':'female'}
for key in dict1:
    print(key,':',dict1.get(key))
print(dict1)
for i in sorted(dict1.items()):
    print(i)
for key in dict1:
    print('value',dict1.get(key))