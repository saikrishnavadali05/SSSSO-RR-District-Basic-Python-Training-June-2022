#Input : Love All Serve All Help Ever Hurt Never
#Write a program to print each word of the line in a new line using both while and for loops.
input_str = "Love All Serve All Help Ever Hurt Never"
input_list = input_str.split(" ")

i = 0
print("using while loop")
while (i < len(input_list)):
    print(input_list[i])
    i = i + 1 

print("using for loop")
for word in input_list:
    print(word)






