import sys
l=[]
for k in sys.argv[1:]:
    l.append(int(k))
Tuple=tuple(l)
RDuplicates=set(Tuple)
print(sum(RDuplicates))