# python code to reverse a string using for loop
def reverse(s):
    str=""
    for i in s:
       str=i+str
       print(str)
    return str

s = "python"
print("The oringinal string is:", s)
#print(s)
print("The reversede string is:", end="")
print(reverse(s))

