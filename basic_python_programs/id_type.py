# Immutable objects does not allow modification after creation

num1 = 10
print(id(num1))
print(type(num1))

num2 = num1

if(id(num1) == id(num2)):
  print("same ids: 1")

if(id(num1) == id(10)):
  print("same ids: 2")

num1 = num1 + 10
print(num1, num2)
print(id(num1), id(num2))
