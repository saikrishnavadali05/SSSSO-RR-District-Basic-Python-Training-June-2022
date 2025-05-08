def mul(l):
    k=1
    for i in l:
        k*=i
    with open('output.txt','w') as f:
        f.write(str(k))
        
