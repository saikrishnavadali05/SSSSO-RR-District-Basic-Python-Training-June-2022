# 4.Write a program to print all the alternative elements of a tuple. 
# The elements to the tuple have to be given to the program using input() function.

Tpl_var = eval(input("Enter a tuple :-"))
tup1 = ()
tup2 = ()

for i in range( len(Tpl_var)) :
    if i % 2 == 0 :
        tup1 += ( Tpl_var[ i ], )
    else :
        tup2 += ( Tpl_var[ i ], )

print("Alternate elements")
print( tup1 )
print( tup2 )