a=int(input("Enter first number"))
b=int(input("Enter second number"))
#maxmum of two numbers"
#using ternary operator
print("Max=", a if a>=b else b)
#using max function
print("max1=",max(a,b))
#using if-else
if a>=b:
    print("max2=", a)
else:
    print("max2=",b)
#minimum of two two numbers
#using ternary operator
print("Min=",a if a<b else b)
#using min function
print("min1=",min(a,b))
#using if else
if a<b:
    print("min2=",a)
else:
    print("min2=",b)
    
#Average of two numbers
average=(a+b)/2
print("Average=",average)
#Addition of two numbers
sum=(a+b)
print("Sum=",sum)
#multiplication of two numbers
product=(a*b)
print("product=",product)
