a=1
b=1.23
d=2+4j
string_number = '56'
f=[1,2,3]
z=(4,5,6)
print("Object identities of all the variables")
print("\n",id(a))
print("\n",id(b))
print("\n",id(d))
print("\n",id(string_number))
print("\n",id(f))
g=int(b)
h=float(a)
i=str(b)
j=int(string_number)
k=tuple(f)
m=list(z)
n=float(d.real)
o=set(f)
list = [g,h,i,j,k,m,n,o]
print(list)

