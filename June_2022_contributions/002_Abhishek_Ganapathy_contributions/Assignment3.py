# Write a program that accepts an integer (n) and computes the value of n+nn+nnn. If n is 5, the output should be 5+55+555 = 615
Integer = int(input("Enter one digit integer "))
Calculate = (1*Integer) + (10*Integer+1*Integer)+(100*Integer+10*Integer+Integer)
print((1*Integer), "+",(10*Integer+1*Integer),"+",(100*Integer+10*Integer+Integer),"=",Calculate)
