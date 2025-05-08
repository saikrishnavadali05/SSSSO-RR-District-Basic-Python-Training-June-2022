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
