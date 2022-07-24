from audioop import mul


print("hello")
# hello (single line comment)

print("DiVya\nrani\nkrish")
'''
DiVya
rani
krish ''' #multiple line comment

print("DiVya","rani","krish", sep=":", end='')
# DiVya:rani:krish (separate expression which separates the strings )

print("DiVya","rani","krish", sep=":", end='*')
# DiVya:rani:krishDiVya:rani:krish* (ended with a character entered in end expression)

print()
print("hello")
print()
print()
print("aneyyo")
'''
hello


aneyyo '''#(output)

# arithmetic operations on python
'''
a=int(input("enter a value "))
b=int(input("enter b value "))
add=a+b
sub=a-b
multiply=a*b
div=a/b
expo=a**b
print(add)
print(sub)
print(multiply)
print(div)
print(expo)
'''
'''
enter a value 8
enter b value 3
11
5
24
2.6666666666666665
512 ''' #output

a=10
b=20
c=a+b
print(a,"+",b,"=",c) # 10 + 20 = 30

print("A mutable object can be changed after \
it is created, and an immutable object \
cannot. Objects of built-in types like")
# A mutable object can be changed after it is created, and an immutable object cannot. Objects of built-in types like (continuation lines)

add=1+2+3\
+4+5+6\
+7+8
print(add) # 36

