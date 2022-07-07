#Write a program to print each word of the line in a new line using both while and for loops.


String = "Love All Serve All Help Ever Hurt Never"
String1 = String.split()

aaap
#Using For loop
for i in String1:
    print(i)

    
#using while loop  
index = 0
while index<len(String1):
    print(String1[index])
    index = index + 1
