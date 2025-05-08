from platform import python_branch
from this import s


Name = "Neeraj_Soni"
print(Name[4])
print(Name[0:6])
a = 400
print("Id of the variable is", id(a))

print("**************$&$************")
#Built-in Function
name1 = "Neeraj_Soni"
name2 = "Sakshi_Rana"
add_name = name2[0:6] + '_' + name1[7:]
print(add_name)
#Name Index
print("Finding the letter index", name1.index('S'))
print(name2.index('Ra'))
print('N' in name1)
print(name1.upper(), name2.upper())
print(name2.replace('Rana','Soni'))
Symbol = "@@-@@"
print(Symbol.join(('Neeraj ',' Sakshi')))
print("Printing name 3 times:  ", name1*3, "\n", "Length of name is: ", len(name1))

#Using Backlash to continue statements
print("--------------------------------------")
a = 5 + \
3*3
b = eval("6.5") + 3
print(type(b))
print(repr(name1))

print("---------Excercise-5--------")
#1
Input_string = "python"
print(Input_string.upper())
#2
print(Input_string.replace('p','c'))
#3
print(Input_string.center(20))
#4
string = "Hello, emma."
result = string.index("e")
print(result)