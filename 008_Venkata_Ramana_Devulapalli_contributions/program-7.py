s=input()
w=s.split(" ")
n=5
q=0
for i in range(1,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(0,(2*i-1)):
        if(k%2==0):
            print("*", end=" ")
        else:
            print(w[q] ,end=" ")
            q+=1
    print()
        