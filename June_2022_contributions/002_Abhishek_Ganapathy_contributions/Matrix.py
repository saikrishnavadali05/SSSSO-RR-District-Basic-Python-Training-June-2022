x = int(input("Enter the x "))
y = int(input("Enter the y "))
Number_List = []
print("The matrix is",x,"x",y)

print("Enter the numbers")

for i in range(0,x):
    Number = []
    for j in range(0,y):
        Number.append(int(input()))
    Number_List.append(Number)

print("Print the Matrix")
for i in range(0,x):
    for j in range(0,y):
        print(Number_List[i][j], end = " ")
    print()

