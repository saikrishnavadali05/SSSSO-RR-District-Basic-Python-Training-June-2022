def reverse(a) :
    str=""
    for k in a:
        str=k+str
    return str
a=input()
print("Reversed string:",end="")
print(reverse(a))
