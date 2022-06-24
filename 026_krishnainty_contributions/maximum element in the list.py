n=int(input("Enter n value"))
p=[]
for i in range(n):
    ele=int(input("enter value"+str(i)+" "))
    p.append(ele)
print("complete list is ",p)
print("maximum element in the list is ",max(p))
