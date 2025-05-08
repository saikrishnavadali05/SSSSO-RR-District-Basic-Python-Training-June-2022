n=int(input("Enter n value"))
p=[]
for i in range(n):
    ele=int(input("enter value"+str(i)+" "))
    p.append(ele)
print("complete list is ",p)
unique=[]
for i in p:
    if(i not in unique):
        unique.append(i)
print("unique list is ",unique)
