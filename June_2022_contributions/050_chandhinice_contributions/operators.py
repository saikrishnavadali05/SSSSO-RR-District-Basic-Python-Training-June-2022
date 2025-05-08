#operators


a = 3+7j
b = 5-9j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#print(a % b) # only integer division is possible for complex case
men = 45
women = 60
print(men < women)
print( men > women)


#exercise 4

number = (45 - 3 ** 3) / 6
print(number)
a = 2
b = 10
c = 6
a += b
b %=c
print(a, b)
print(c > b)
print(a == (a + b + c) - 20)
d = a < c or a != 12
print(d)