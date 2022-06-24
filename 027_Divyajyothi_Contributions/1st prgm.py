#Write a program to print each word of the line in a new line using both while and for loops.
#Input : Love All Serve All Help Ever Hurt Never
#Using While loop
input_1 = "Love All Serve All Help Ever Hurt Never"
while ' ' in input_1:
    i = input_1.index(' ')
    print(input_1[:i])
    input_1 = input_1[i+1:]
print(input_1)
#Using for loop
string_1="Love All Serve All Help Ever Hurt Never"
for i in string_1:
    print(i,end='')
    if(i==" "):
        print()