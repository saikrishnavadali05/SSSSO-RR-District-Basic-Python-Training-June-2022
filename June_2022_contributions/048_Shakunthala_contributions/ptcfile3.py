# range
for i in range(1,7):
    print(i, " ", i * i)
print()
for i in range(0, 15, 2):
    print(i, " ", i * i)
print()
print(list(range(0, -8, -2)))

# out put
#2   4
#4   16
#6   36
#8   64
#10   100
#12   144
#14   196

#[0, -2, -4, -6]

#Set's
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
my_set.remove(1)
print(my_set)
#output
#{2,3,4} 

#Tuples

X = [10,20,30]
Y = [50,"Python","JournalDev"] 
print(len(X),max(X),min(X)) # 3 30 10
Z = (X+Y)
print(Z)
#[10, 20, 30, 50, 'Python', 'JournalDev']
print(20 in X)
#true

#Slicing Operator in Lists and Strings

numbers =[0,1,2,3,4,5,6]
print(numbers[2:5])
#[2,3,4]
print(numbers[2:5:2])
print(numbers[-1:-5:-2])
#[2, 4]
#[6, 4]

#Dictionary

person = {'name': 'ram','age': 20,'group':'B.sc'}

print(person['name'])


print(len(person))

for key in person.keys():
    print(key)

 
for value in person.values():
    print(value)


for key, value in person.items():
    print(key, value)
#ram
#3
#name
#age
#group
#ram
#20
#B.sc
#name ram
#age 20
#group B.sc

#OrderedDict
from collections import OrderedDict
od = OrderedDict()
od['x'] = 3
od['y'] = 2
od['z'] = 4
print(od.items())
d = {}
d['x'] = 3
d['y'] = 2
d['z'] = 4
print(d.items())
#odict_items([('x', 3), ('y', 2), ('z', 4)])
#dict_items([('x', 3), ('y', 2), ('z', 4)])

for key, value in od.items():
    print(key, value)
print("\nAfter deleting:")
od.pop('z')
for key, value in od.items():
    print(key, value)
print("\nAfter re-inserting:")
od['z'] = 4
for key, value in od.items():
    print(key, value)
#x 3
#y 2
#z 4

#After deleting:
#x 3
#y 2
#After re-inserting:
#x 3
#y 2
#z 4

#Python Functions

#User define function

def square(a):
 return a * a

val = square(4)
print(val)
print(type(val))

val = square
print("val(2)",val(2))
#16
#<class 'int'>
#val(2) 4