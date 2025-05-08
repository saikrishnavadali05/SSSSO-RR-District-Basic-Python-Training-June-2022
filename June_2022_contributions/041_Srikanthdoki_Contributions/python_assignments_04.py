t = (input ("Enter a elements for tuple :-"))  #EVAL IS TO PICK THE VALUES IN LIST
tup1 = ()
tup2 = () 
for i in range (len (t)) :
    if i % 2 == 0 :
        tup1 += (t[ i ],)
    else :
        tup2 += (t[ i ],)
print("Alternate elements") 
print (tup1)
print (tup2)