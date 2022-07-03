# The data types in python which can be iterated through are iterable data types.
# Types like Lists, Sets, Tuples, Strings, etc... are iterable.

name = 'Prashanth'

# we can create an iterator to iterate the above iterable type (name) using iter() method.

my_iterator = iter(name)

# next() method is used to access the following value of the iterable type.

print(next(my_iterator)) # P
print(next(my_iterator)) # r
print(next(my_iterator)) # a
print(next(my_iterator)) # s
print(next(my_iterator)) # h
print(next(my_iterator)) # a
print(next(my_iterator)) # n
print(next(my_iterator)) # t
print(next(my_iterator)) # h

