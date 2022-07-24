#occurence of an integer in a linked list

n=int(input())
l=list(map(int,input().split()))
m=int(input())
if m in l:
    print(l.count(m))
else:
    print(0)