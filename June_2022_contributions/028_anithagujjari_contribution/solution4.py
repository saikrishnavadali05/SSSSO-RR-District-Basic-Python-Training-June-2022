n=input("enter elements seperated by ,")
list1=n.split(',')
tuple1=tuple(list1)
for i in range(0,len(tuple1),2):
    print(tuple1[i])
