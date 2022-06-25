#Question1:Write a program to print each word of the line in a new line using both while and for loops.
#Input : Love All Serve All Help Ever Hurt Never

Input = ['Love','All','Serve','All','Help','Ever','Hurt','Never']
print("print for loop execution")
for i in range(8):
    print(Input[i])
print("print while loop execution")
a=0
while a<8:
    print(Input[a])
    a+=1