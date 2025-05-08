num = int(input("Enter a number: "))
#123 = 1+2+3
s = 0
mod = 0
while num>0:
    mod = num%10
    s += mod
    num= num//10
print(s)