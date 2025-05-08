
a=input("enter elements seperated by ,")
b=a.split(',')
tuple1=tuple(b)
for i in range(0,len(tuple1),2):
    print(tuple1[i])