print("6. Write a program to pass a list as a command line arguments. \
Next, convert that list into a tuple after removing all the duplicate elements.(hint : use set) \
Next, add all the elements of that duplicate free tuple and print \
the addition output.")

x = [1,2,3,2,4,3,5,2,3,6,4,5]
print("type of x is: ", type(x),x)
t1 = tuple(x)
print(t1)
t2 = set(t1)
print(t2)

print("sum of the touple values is", sum(t2))
