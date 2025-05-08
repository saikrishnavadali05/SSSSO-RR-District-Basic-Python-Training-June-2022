strg = input("Enter a string:")
upper = ""
lower = ""
num = ""
for i in strg:
    if i.isupper():
        upper = upper+i
    elif i.islower():
        lower = lower+i
    else:
        num = num+i
print(upper, len(upper), end="\n")
print(lower, len(lower), end="\n")
print(num, len(num), end="\n")
    