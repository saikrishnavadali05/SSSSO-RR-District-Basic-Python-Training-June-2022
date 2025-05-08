#numeric Datatype
#Integer Datatype
i=20
#Float Datatype
b=30.0
#Complex Datatype
c=20+30j
#String Datatype
str="Sai Ram"
#list
lst=[1,2,3]
#tuple
tpl=(4,5,6)
#bool
bl=True
#printing object ids
print(id(i))
print(id(b))
print(id(c))
print(id(str))
print(id(lst))
print(id(tpl))
print(id(bl))
#type acasting
i=float(i)
b=int(b)
c=c.real
str=list(str)
lst=tuple(lst)
tpl=list(tpl)
b1=int(bl)
new_list=[i,b,c,str,lst,tpl,bl]
print(new_list)



# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> Python assignment8.py
# 1796850844496
# 1796851882416
# 1796851881904
# 1796852134320
# 1796852233984
# 1796852225216
# 140720792513384
# [20.0, 30, 20.0, ['S', 'a', 'i', ' ', 'R', 'a', 'm'], (1, 2, 3), [4, 5, 6], True]
# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> 