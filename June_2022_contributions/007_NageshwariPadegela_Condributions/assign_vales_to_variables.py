# Basic Form - This is the most commonly used form of asssignment
print("\n'Basic Form' of Assignment")
a = 5 #a[memory location] = 5[expression]
print(a)
print(type(a))
b = 'Hello'
print(b)
print(type(b),'\n')

# Tuple Assignment
print('Tuple Assignment')
n1, n2 = (10, 20)
print(n1)
print(n2)
print(type(n1))
print(type(n2), '\n')

# List Assignment
print('List Assignment')
a1, a2 = ['hello', 'world']
print(a1)
print(type(a1))
print(a2)
print(type(a2), '\n')

# Sequence Assignment - any sequence of names can be assigned to any sequence of values, and python assigns the items one at a time by position
print("Sequence Assignment")
a, b, c = 'hii'
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c), ' \n')

# Extented Sequence unpacking - It allows us to be more flexible in how we select portions of a sequence to assign.
print("Extented Sequence Unpacking")
p, *q = 'hello'
print(p)
print(type(p))
print(q)
print(type(b), '\n')

# Ex2
p, *q, r = 'OM SAI RAM'
print(p)
print(q)
print(r, '\n')

# Ex3
# x, *y, z, *a = 'hello world' Here it throws an error two variables unpacking is not possible at once.

# Multiple Target Assignment 
print("Multiple Assignment")
x = y = z = 10
print(x, y, z, sep = '\n')

# Augmented Assignment
print('\nAugmented Assignment')
x = 8
x += 1
print(x,'\n')

y = 9
y -= 1
print(y,'\n')

z = 10
z *= 10
print(z)




