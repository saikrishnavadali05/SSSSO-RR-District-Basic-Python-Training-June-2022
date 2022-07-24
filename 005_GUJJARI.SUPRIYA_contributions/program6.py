import sys
'''problem statement:Write a program to pass a list as a command line arguments.
 Next, convert that list into a tuple after removing all the duplicate elements. 
 (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.'''
list1=[]
for i in sys.argv[1:]:
    list1.append(int(i))
tuple1=tuple(list1)
set1=set(tuple1)
print(sum(set1))
