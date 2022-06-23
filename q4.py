#Q4.Write a program to print all the alternative elements of a tuple.
#  The elements to the tuple have to be given to the program using input() function.

# By Using while Loop Method 
tup = eval(input("Enter input for tuple:"))
tup2 = ()
tup3 = ()
i = 0
while i < len(tup):
    if i % 2 == 0:
        tup2 += (tup[i],)
    else:
        tup3 += (tup[i],)
    i += 1
print(tup2)
print(tup3)

#output 1
#Enter input for tuple:(0,1,2,3,4,5,6,7,8,9)
#(0, 2, 4, 6, 8)
#(1, 3, 5, 7, 9)

#output2
#Enter input for tuple:('DNYANESHWAR')
#('D', 'Y', 'N', 'S', 'W', 'R')
#('N', 'A', 'E', 'H', 'A')



# By Using For Loop Method 

T = eval(input("Enter a tuple :-"))
tup1 = ()
tup2 = ()
for i in range( len(T)) :
    if i % 2 == 0 :
        tup1 += ( T[ i ], )
    else :
        tup2 += ( T[ i ], )
print("Alternate elements")
print( tup1 )
print( tup2 )


#OUTPUT1
#Enter input for tuple:('0123456789')
#('0', '2', '4', '6', '8')
#('1', '3', '5', '7', '9')

#OUTPUT2
#Enter input for tuple:('SAIRAM SIR')
#('S', 'I', 'A', ' ', 'I')
#('A', 'R', 'M', 'S', 'R')
