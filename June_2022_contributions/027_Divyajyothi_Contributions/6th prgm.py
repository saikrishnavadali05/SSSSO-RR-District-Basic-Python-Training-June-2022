x=[1,5,9,7,5,3,1,9,5,7,3]
print(type(x))
t1=tuple(x)
print(t1)
t2=tuple(set(t1))
print(t2)
print("addition od tuple is:",sum(t2))