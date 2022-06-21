#Write a program to pass a list as a command line arguments. 
#Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) 
#Next, add all the elements of that duplicate free tuple and print the addition o

list=[1,2,3,4,7,1,2,3,5,6,7,6]
print(list)
tuple1=tuple(list)
print(tuple1)
tuple2=tuple(set(tuple1))
print(tuple2)
tuple3=tuple2
#to add the elements of tuple use list() and sum() funtion.
A = [int(i) for i in tuple3]
  
b = 0
  
for i in A:
    b += i
print("sum of all the tuple members is ", b)