t=()
n=int(input()) ##length of tuple
l=[]
for i in range(0,n):
    m=int(input())
    l.append(m)
t=t+(tuple(l))
print(t)
for i in range(len(t)):
    if(i%2==0):
        print(t[i])