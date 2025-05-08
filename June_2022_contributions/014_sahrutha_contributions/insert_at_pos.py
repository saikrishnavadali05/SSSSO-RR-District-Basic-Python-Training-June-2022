#insertion of element at a given position

n=int(input())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
m=p[0]
for i in range(n+1):
    if i<=m:
        print(l[i],end=" ")
    if i==m+1:
        print(p[1],end=" ")
    if i>m+1:
        print(l[i],end=" ")