# 6.Write a program to pass a list as a command line arguments. 
# Next, convert that list into a tuple after removing 
# all the duplicate elements. (hint : use set) 
# Next, add all the elements of that duplicate 
# free tuple and print the addition output.
from sys import argv

List_1 = []

for i in argv:
    List_1.append(int(i))

tpl = tuple(List_1)

# Removing the all the duplicates.
dpl = set(tpl)

#sum of the tuple after duplicate free tuple.

print(sum(dpl))






