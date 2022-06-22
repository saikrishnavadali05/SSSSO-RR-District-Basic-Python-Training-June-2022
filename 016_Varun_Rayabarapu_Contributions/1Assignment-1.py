#Write a program to print each word of the line in a new line using both while and for loops.
#using for loop
sen=input("enter the sentence-")
for i in range(len(sen)):
    if sen[i]==" ":
        sen=sen[:i]+"\n"+sen[i+1:]
print(sen)

        
