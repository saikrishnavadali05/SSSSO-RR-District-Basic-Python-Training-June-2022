#8.Write a program to check if the input string is a palindrome? Next, Make the program to work on integers as well. Write a palindrome function. Call that function of 5 different inputs to test whether the function is written properly or not.
def ispalindrome(str):
    for i in range(0, (len(str)//2)):
        if str[i] == str[len(str)-i-1]:
            return True
    return False
str1 = "developprogramme"
str2 = "skillsonprogramme"
str3 = "234153"
str4 = "srikanth"
str5 = "657435"
list = [str1, str2, str3, str4, str5]

for i in list:
    if ispalindrome(i):
        print("{0} is palindrome".format(i))
    else:
        print("{0} is not palindrome".format(i))