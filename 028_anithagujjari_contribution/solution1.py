string_name=" Love All Serve All Help Ever Hurt Never"
print("\nusing for\n")
for i in string_name:
    print(i,end='')
    if(i==" "):
        print()
i=0
print("\nusing while")
while i<len(string_name):
    print(string_name[i],end='')
    if(string_name[i]==" "):
        print()
    i+=1
