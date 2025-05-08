# input() - this function is used to read the data from the user
# this function reads the user input in the string formate

Name = input("Please Enter your name: ")
age = input("Please Enter Your age: ")
print(type(Name))
print(type(age))

# If we want the input in a paticular formate rather than string we have to type-castting it
age = int(input("Please Enter Your Age: "))
print(type(age))

# Multiple Inputs in one line when we typecast the variable as integer
x, y = map(int, input().split())
print(type(x))
print(type(y))
sum = x + y
print(sum)








