#program for printing the alternate elements of a tuple T
T=eval(input("enter a tuple :"))
tup1=()
tup2=()
for i in range(len(T)):
    if i%2== 0:
        tup1 +=(T[i],)
    else :
        tup2 +=(T[i],)
print("alternate elements")
print(tup1)
print(tup2)


