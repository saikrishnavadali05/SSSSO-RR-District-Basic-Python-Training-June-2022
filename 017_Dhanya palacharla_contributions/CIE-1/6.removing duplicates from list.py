list=[1,5,1,8,1,6,3,4,3,4,]
print("original list is:",list)
print("after removing duplicates:",set(list))
tupl=tuple(set(list))
print("tuple is:",tupl)
print("sum of elements in tuple is:",sum(tupl))