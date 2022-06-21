i = 7
while i > 0:
    print("i is", i)
    i = i - 1
    print("loop executed")

#For loop
name = "Neeraj_Soni"
for r in name:
    print(r)

# For loop usinf F
n ="Neeraj_Soni"
print(str(n))
print(repr(n))

for m in range(1, 4):
    print(str(m).rjust(2), str(m*m).rjust(5), sep=":", end=" ")
    print(str(m*m*m).rjust(4), end=" ")
    print(str(m*m*m*m).rjust(4), end=" ")
    print(str(m*m).rjust(6))

print("**************")
for b in range(1,8):
    print('{0:2d} {1:4d} {2:4d}'.format(b,b*b,b*b*b))

print("------$------")
print('12'.zfill(10))

#for loop help n lists
My_Lisrs = ['Carrot', 'Potato', 'Tomato']
for g in My_Lisrs:
    print("To Get from the market:", g)

name =[]
for g in My_Lisrs:
    if len(g) > 5: name.insert(0, g)
    print(name)

months = ['jan','feb','march','april']
for p in range(4):
    print(f"month {p+1}:", (months[p]))

   