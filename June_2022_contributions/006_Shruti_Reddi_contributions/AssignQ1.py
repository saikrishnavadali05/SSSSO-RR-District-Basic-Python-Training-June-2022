# Write a program to print each word of the line in a new line using both while and for loops. 
#input: Love All Serve All Help Ever Hurt Never
#Output : 
#Love
#All
#Serve 
#All 
#Help
#Ever
#Hurt
#Never

#using while loop
#input_string="Love All Serve All Help Ever Hurt Never"
#while ' ' in input_string:
    #i = input_string.index(' ')
    #print(input_string[:i])
    #input_string = input_string[i+1:]
#print(input_string)

#using for loop
input_string="Love All Serve All Help Ever Hurt Never"

for i in input_string.split():
    print(i)