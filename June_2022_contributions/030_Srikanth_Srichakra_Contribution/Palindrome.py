#Checks the given string is a palindrome or not
strng = input ("Enter a string:")
rev_str = strng[::-1]
if strng == rev_str:
    print("Given string '"+strng+"' is a palindrome")
else:
    print("Given string is NOT a palindrome")
    