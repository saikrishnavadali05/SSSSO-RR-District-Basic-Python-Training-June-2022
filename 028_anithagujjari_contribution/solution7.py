'''problem solutin:
              *
         * python *
        * is * a *
      * good * programing * language *
     * to * learn * for * beginners * '''
     list1=['python','is','a','good','programming','language','to','learn','for','beginners']
     rowcount=5
     row=1   

j=0
while(row<=rowcount):
    i=1
    while(i<=(rowcount-row)):
        print(" ",end=' ')
        i+=1
    i=1
    while(i<=2*row -1):
        if(i%2==0):
            print(list1[j],end=' ')
            j+=1
        else:
            print("*",end=' ')
        i+=1
    print('\n')
    row+=1
