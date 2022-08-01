import add
import multiply

try:
    a,b,c,d=map(int,input("Enter four numbers").split())
    for i in a,b,c,d:
        if(i % 2 == 0):
            file = open("output.txt", "w") #writing
            file.write("Addtion Of four number is :")
            file.write(str(add.addition(a,b,c,d)) )
            file.close()
            file = open("output.txt", "a") #writing
            file.write("\n Multiplication Of four number is :")
            file.write(str(multiply.multiplication(a,b,c,d)))
            file.close()
        else:
            print("Argument contain Odd number:",i)

except:
    print("argument should be 4")

