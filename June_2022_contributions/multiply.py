def mulnumbers(num1,num2,num3,num4):

    # check whether the number is even or odd
    if (num1 % 2) == 0:
        print("num1 is even")
        r1=(num1*1)
    else: 
        r1=1
        print("num1 is odd")
        

    if (num2 % 2) == 0:
        r2=(num2*1)
        print("num2 is even")
    else: 
        r2=1
        print("num2 is odd")
        

    if (num3 % 2) == 0:
        print("num3 is even")
        r3=(num3*1)
    else: 
        r3=1
        print("num3 is odd")
        
    
    if (num4 % 2) == 0:
        print("num4 is even")
        r4=(num4*1)
    else: 
        r4=1
        print("num4 is odd")
        


    result=( r1 * r2 * r3 * r4)
    print("the even numbers multiplied result is ", result)
    
    return (result)