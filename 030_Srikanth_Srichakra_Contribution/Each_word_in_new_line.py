'''
1.	Write a program to print each word of the line
in a new line using both while and for loops.

'''
txt = "Love All Serve All Help Ever Hurt Never"

x = txt.split()

print("Using for loop:")
for word in x:
    print(word)

print()
print("Using while loop:")

i=0
while i<len(x):
        print(x[i])
        i=i+1