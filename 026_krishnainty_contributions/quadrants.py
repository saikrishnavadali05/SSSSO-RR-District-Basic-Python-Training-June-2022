x=int(input("Enter x value"))
y=int(input("Enter y value"))

if(x>0):
    if(y>0):
        print(x,y,"belongs to Q1")
    else:
        print(x,y,"belongs to Q4")
else:
    if(y>0):
        print(x,y,"belongs to Q2")
    else:
        print(x,y,"belongs to Q3")
    
