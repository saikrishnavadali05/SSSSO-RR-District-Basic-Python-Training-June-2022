#To delete middle element of a list

n=int(input())
m=list(map(int,input().split( )))
l=int(n/2)
for i in range(n):
    if i<l:
        print(m[i],end=" ")
    if i==l:
        print(end="")
    if i>l:
        print(m[i],end=" "