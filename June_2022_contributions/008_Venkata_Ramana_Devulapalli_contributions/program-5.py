d={}
n=int(input())  ##the length of the dictionary
for i in range(0,n):
    k,v=input().split(" ")
    d.update({k : v})
## Retrieving the values from Keys
for i in d:
    print(d.get(i))
##Printing full dictionary
print("/////////////////////////")
print(d)
print("/////////////////////////")
## printing key and values pairs
for i in d:
    v=d.get(i)
    print(i," : ",v)

    