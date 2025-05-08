#Write a program to print each word of the line in a new line using both while and for loops.

str = "Love All Serve All Help Ever Hurt Never"
print(str)
str1=list(str.split())
print(str1)
for i in str1:
    print(i)
'''(output)
Love All Serve All Help Ever Hurt Never
['Love', 'All', 'Serve', 'All', 'Help', 'Ever', 'Hurt', 'Never']
Love
All
Serve
All
Help
Ever
Hurt
Never
'''
#(Here the string must convert into a list then split to print each word in a new line.)

for i in str:
    print(i)
'''
Output:
L
o
v
e

A
l
l

S
e
r
v
e

A
l
l

H
e
l
p

E
v
e
r

H
u
r
t

N
e
v
e
r
#(printing each letter in separate line)
'''