num=int(input())
def fac(num):
    facc=1
    if num>1:
        for i in range(1,num+1):
            facc=facc*i
        print(facc)
    elif num==0:
        print(1)
    else:
        print("no factorial for negative numbers")
fac(num)