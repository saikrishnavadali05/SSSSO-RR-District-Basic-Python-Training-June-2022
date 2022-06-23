num=int(input())
p=() 
l=[]
for i in range(0,num):
    m=int(input())
    l.append(m)
p=p+(tuple(l))
print(t)
for i in range(len(t)):
    if(i%2==0):
        print(p[i])