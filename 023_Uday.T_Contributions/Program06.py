#Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.
#Solution
list=[15,1,5,6,2,4,5,3,7,5,8,9,10,15,4,1]
print(list)
tuple_d=tuple(list)
print(tuple_d)
tuple_r=tuple(set(tuple_d))
print(tuple_r)
tuple_y=tuple_r
#to add the elements of tuple use list() and sum() funtion.
u = [int(i) for i in tuple_y]
  
e = 0
  
for i in u:
    e += i
print("sum of all the duplicate free tuple numbers is ", e)