# Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.
String = (input("Enter the string "))
Flag = False
Count = 0
Uppercase = String.upper()
print("The upper case of the string",String,"is",Uppercase)
Lowercase = String.lower()
print("The upper case of the string",String,"is",Lowercase)
Length = len(String)
print("Length of the string",String,"is",Length)
for i in String:
    if (i.isdigit()):
        Count = Count + 1
print("Number of digit in String", String,"is",Count)



