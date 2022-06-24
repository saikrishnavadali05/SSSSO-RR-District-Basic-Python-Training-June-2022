dict_1={'name':'anitha','rollno':'41','gender':'female'}
for key in dict_1:
    print(key,':',dict_1.get(key))
print(dict_1)
for i in sorted(dict_1.items()):
    print(i)
for key in dict_1:
    print('value',dict_1.get(key))