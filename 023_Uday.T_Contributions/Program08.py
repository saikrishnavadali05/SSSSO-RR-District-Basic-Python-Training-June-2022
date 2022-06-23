#Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.
#solution
int_1 = 7
print(int_1)
float_1 = 0.5
print(float_1)

list_1 = ['Om', 'Sri', 'Ram', 'Krishna lord', 'Uday', 'you']
print(list_1)
string_1 = 'This is not a string.'
print(string_1)
tuple_1 = ('sri', 'ram', 'das', 'great', 'you', 'are')
print(tuple_1)
dict_1 = {
	"yes": "he",
	"no": "She",
	"you": "his",
	"right": "left",
	"corner": "centre",
	"fish": "water"
}
print(dict_1)    
set_1 = {"do", "this", "that", "not", "do", "python"}
 
for y in set_1:
	print(y)

u=float(int_1)
print(u)

v=int(float_1)
print(v)
w=tuple(string_1)
print(w)
new_list_is=[u,v,w]
print(new_list_is)