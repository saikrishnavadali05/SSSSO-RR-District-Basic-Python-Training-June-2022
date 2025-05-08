string = input("Enter the string")
character = input("Enter the character")
#This can be done using slicing
string = string[:0]+character+string[1:]
print(string)