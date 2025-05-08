x = input('Enter the tuple : ')
x = tuple(int(a) for a in x.split(","))
print(x)
tup1 = ()
tup2 = ()
for i in range( len(x)) :
    if i % 2 == 0 :
        tup1 += ( x[ i ], )
    else :
        tup2 += ( x[ i ], )
print("Alternate elements")
print( tup1 )
print( tup2 )