n=input("enter elements seperated by ,")
list1=n.split(',')
t1=tuple(list1)
for i in range(0,len(t1),2):
    print(t1[i])
