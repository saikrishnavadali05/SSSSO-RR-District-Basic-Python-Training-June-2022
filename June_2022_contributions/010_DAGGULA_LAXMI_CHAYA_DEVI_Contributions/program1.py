#program to print each word of the line in a new line using both while and for loops
#get input from user
string=input('Enter a string:')
#using while loop
while ' ' in string:
    i=string.index(' ')
    print(string[:i])
    string=string[i+1:]
print(string)
#using for loop
string2=input('Enter a string:')
for s in string2.split():
    print(s)
