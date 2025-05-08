# To get the output we have to use the print() function.

print("Welcome to Python Programming Language.")

message = "Good Morning"
print('message is', message)

# Priting the output in different lines
# M1
print("Hello")
print("Welcome to Python Programming Language")
print("Happy Learning\n")

# M2
print("Hello", "Welcome to Python Programming Language", "Happy Learning")
print("Hello", "Welcome to Python Programming Language", "Happy Learning", sep = '\n')
print("\nHello", "Welcome to Python Programming Language", "Happy Learning", sep = '-')

# M3
# We can even use ''' ''' to print in different lines
print('''\nHello 
Good Morning
Have a nice day..!!
''')

# Two print statements in same line 
print("Hello World", end = ". ")
print("Good Morning")

# In Python also we can use format specifiers
name = "Nag"
age = 19
print("This is %s, my age is %d"%(name, age))

a = 10
b = 3
c = a/b
print("%d by %d is %.2f"%(a, b , c))

