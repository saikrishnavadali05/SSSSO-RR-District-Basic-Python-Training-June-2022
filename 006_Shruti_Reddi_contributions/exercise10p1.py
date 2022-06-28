#Write a function that take string as a parameter. the string is given by the user as input. the final output from the function is to reverse the string.
# example the string is Multiple - output is elpitluM
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input('Enter a string :')
 
print ("The original string is : ",end="")
print (s)
 
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))