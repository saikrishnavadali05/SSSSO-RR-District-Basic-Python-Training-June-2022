list=[]
n=int(input("enter the no. of elements"))
for i in range(0,n):
    elements=int(input())
    list.append(elements)
tupl=tuple(list)
print("elements in tuple are:",tupl)
print("alternative elements in tuple are:",tupl[ : :2])
  