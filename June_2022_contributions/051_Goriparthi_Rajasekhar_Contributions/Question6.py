#Question6 : Write a program to pass a list as a command line arguments.
# Next, convert that list into a tuple after removing all the duplicate elements. 
# (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

list=[1,2,3,4,5,6,7,1,6,3,8,9,10,4]
print(list)
Tuple_Var=tuple(list)
print(Tuple_Var)
Tuple_Rem=tuple(set(Tuple_Var))
print(Tuple_Rem)
tuple_y=Tuple_Rem
#to add the elements of tuple use list() and sum() funtion.
Num = [int(i) for i in tuple_y]
  
Sum = 0
  
for i in Num:
    Sum += i
print("Sum of all the duplicate free tuple numbers = ", Sum)