#Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

from sys import argv


input_list=argv[1:]

print("Before Set",input_list)
input_list=set(input_list)
print("After Set",input_list)

tuple1=tuple(input_list)
print("after converting it into tuple",tuple1)
print(type(tuple1))

