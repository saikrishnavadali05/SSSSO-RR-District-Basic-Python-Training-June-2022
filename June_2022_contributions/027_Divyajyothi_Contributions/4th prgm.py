# fINDING ALTERNATE ELEMENTS IN A TUPLE
T = eval (input ("Enter a tuple :-"))  #EVAL IS TO PICK THE VALUES IN TUPLE
tup1 = ()
tup2 = () 
for i in range (len (T)) :
    if i % 2 == 0 :
        tup1 += (T[ i ],)
    else :
        tup2 += (T[ i ],)
print("Alternate elements") 
print (tup1)
print (tup2)