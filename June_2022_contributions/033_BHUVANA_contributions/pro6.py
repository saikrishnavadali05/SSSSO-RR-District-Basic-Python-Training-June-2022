import sys
a=[]
for i in sys.argv[1:]:
    a.append(int(i))
tuple1=tuple(a)
set1=set(tuple1)
print(sum(set1))
