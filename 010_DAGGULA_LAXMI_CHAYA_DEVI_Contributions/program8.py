#numeric Datatype
#int
a=10
#float
b=20.0
#complex
c=10+20j
#string
str="hello world"
#list
lst=[4,5,6]
#tuple
tpl=(1,2,3)
#bool
bl=True
#printing object ids
print(id(a))
print(id(b))
print(id(c))
print(id(str))
print(id(lst))
print(id(tpl))
print(id(bl))
#type acasting
a=float(a)
b=int(b)
c=c.real
str=list(str)
lst=tuple(lst)
tpl=list(tpl)
b1=int(bl)
new_list=[a,b,c,str,lst,tpl,bl]
print(new_list)


