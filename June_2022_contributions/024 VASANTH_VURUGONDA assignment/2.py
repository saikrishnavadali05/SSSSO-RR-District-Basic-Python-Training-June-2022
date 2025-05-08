a=int(input("Enter first number"))
b=int(input("Enter second number"))

print("Max=", a if a>=b else b)
print("max1=",max(a,b))
if a>=b:
    print("max2=", a)
else:
    print("max2=",b)

print("Min=",a if a<b else b)
print("min1=",min(a,b))
if a<b:
    print("min2=",a)
else:
    print("min2=",b)
average=(a+b)/2
print("Average=",average)
sum=(a+b)
print("Sum=",sum)
product=(a*b)
print("product=",product)