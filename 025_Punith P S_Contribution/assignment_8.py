#Write a program to create variables storing values for each datatype. print the object identities 
# of all the created variables. Next, convert the types of the each varible into another type. 
# After changing the type, store all the values of all the variables in a list. Finally, Print the list.
int_num = 123
float_num = 2.33454
bool_var = False
str_var = "sai ram"
lst_var = [1,2,4,"om",6]
tpl_var = (12, 5, 8)
dict_var = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
name_set = {"Harish", "Ramesh", "Suresh"}

print(id(int_num))
print(id(float_num))
print(id(bool_var))
print(id(str_var))
print(id(lst_var))
print(id(tpl_var))
print(id(dict_var))
print(id(name_set))


float_num = float(int_num)
int_num = int(float_num)
str_var = str(lst_var)
lst_var = list(tpl_var)
tpl_var = tuple(dict_var)
#dict_var = dict(name_set)
#name_set = set(int_num)


new_lst = []
new_lst.append(float_num)
new_lst.append(int_num)
new_lst.append(str_var)
new_lst.append(lst_var)
new_lst.append(tpl_var)
new_lst.append(name_set)
new_lst.append(bool_var)

print(new_lst)