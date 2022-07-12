Enter_String = str(input("Enter the string "))
Enter_String_Reverse = Enter_String[::-1]
print("The String is ",Enter_String)
print("The reverse of the given string is ",Enter_String_Reverse)
if Enter_String == Enter_String_Reverse:
    print("This string is palindrome")
else:
    print("This string is not a palindrome")

print("Using Function")
def Check_palindrome(String):
    Enter_String_Reverse1 = String[::-1]
    if String == Enter_String_Reverse1:
        print("This string is palindrome")
    else:
        print("This string is not a palindrome")

Enter_String1 = str(input("Enter the string "))
Check_palindrome(Enter_String1)