a=[]
n=int(input("Enter the range of list"))
for i in range(n):
    element=int(input("Enter the element"))
    a.append(element)
print("Now we will change the list into tuple")
a = tuple(a)
print(type(a))
print("To print the alternate elements in the tuple")
print(a[0:n:2])

 