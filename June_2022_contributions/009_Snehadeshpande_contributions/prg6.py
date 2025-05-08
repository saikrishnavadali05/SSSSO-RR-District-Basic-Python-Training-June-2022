import sys
list1=[]
for i in sys.argv[1:]:
    list1.append(int(i))
tuple1=tuple(list1)
set1=set(tuple1)
print(sum(set1))