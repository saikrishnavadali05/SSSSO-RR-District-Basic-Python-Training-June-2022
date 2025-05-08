def Mul(a,b,c,d):
if(a%2==0):
    if(b%2==0):
        if(c%2==0):
            if(d%2==0):
                return (a+b+c+d)
    elif(c%2==0):
            if(d%2==0):
                return (a+c+d)
elif(b%2==0):
        if(c%2==0):
            if(d%2==0):
                return (b+c+d)
elif(c%2==0):
    if(d%2==0):
        return (c+d)
elif(d%2==0):
    return(d)
else:
    print("all the variables are odd")

