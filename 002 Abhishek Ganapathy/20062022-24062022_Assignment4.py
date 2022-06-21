# Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.
Tuple = tuple(input("Enter Numbers "))
print("The tuple is",Tuple)
Alternate_Numbers = []
print("The lenght of the tuple is", len(Tuple))
for i in range(0,len(Tuple)):
   if i%2 == 0: 
      # print(Tuple[i])
      Alternate_Numbers.append(Tuple[i])
print("The Alternate numbers are", Alternate_Numbers)



