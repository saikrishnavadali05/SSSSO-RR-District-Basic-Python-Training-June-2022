n=eval(input("Enter input for tuple:"))
n2=()
n3=()
i=0
while i<len(n):
  if i%2 == 0:
    n2 += (n[i],)
  else:
    n3 += (n[i],)
  i += 1
print(n2)
print(n3)



