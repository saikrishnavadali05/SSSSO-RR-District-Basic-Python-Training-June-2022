#reversing a string in seperatre function

def reversestring(str):
    string=str[::-1]
    return string

str=input("Enter any string")
string=reversestring(str)
print("{0}:{1}".format(str,string))
