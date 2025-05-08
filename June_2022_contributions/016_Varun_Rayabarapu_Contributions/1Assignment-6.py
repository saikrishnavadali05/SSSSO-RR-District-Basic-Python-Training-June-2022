#Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.
li=list(map(int,input("enter list of integers with space - \n").split()))
li=set(li)
li=tuple(li)
print("sum of non duplicates is : ",sum(li))
