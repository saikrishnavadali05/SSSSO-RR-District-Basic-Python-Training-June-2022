#Write a program to print each word of the line in a new line using both while and for loops.
#using while loop
sen=input("enter the sentence-")
i=0
while i<len(sen):
    if sen[i]==" ":
        sen=sen[:i]+"\n"+sen[i+1:]
    i+=1
print(sen)
