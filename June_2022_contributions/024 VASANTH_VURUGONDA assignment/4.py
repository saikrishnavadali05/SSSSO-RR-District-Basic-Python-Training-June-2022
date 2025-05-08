#tuple Alternative elements
tpl=input("Enter the tuple elements:")
tpl=tuple(int(a) for a in tpl.split())
print(tpl)
print("Tuple chain 1:",tpl[0::2])
print("Tuple chain 2:",tpl[1::2])