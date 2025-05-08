# Write a program to check if the input string is a palindrome?
String = input("Enter the string to check if its a palindrome ")
Reverse_String = String[::-1]
print("The string is",String,"and the reversed string is",Reverse_String)
if String != "":
    if(String == Reverse_String):
        print("The String is palindrom")
    else:
        print("The String is not a palindrom")

