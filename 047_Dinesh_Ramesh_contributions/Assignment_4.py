#Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.






T = tuple(input("Enter a tuple :-"))
tuple_1 = ()
tuple_2 = ()
i=0
for i in range(len(T)) :
    if i % 2 == 0 :
        tuple_1 += (T[i],)
    else:
        tuple_2 += (T[i],)
    
print("Alternate elements")
print(tuple_1)
print(tuple_2)
