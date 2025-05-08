# program to check whether input string is a palindrome

# defining function palindrome
def ispalindrome(str):
    for i in range(0, (len(str)//2)):
        if str[i] == str[len(str)-i-1]:
            return True
    return False


# checking the function with 5 inputs
str1 = "madam"
str2 = "chaya"
str3 = "12321"
str4 = "AMMA"
str5 = "NANNA"
lst = [str1, str2, str3, str4, str5]

for i in lst:
    if ispalindrome(i):
        print("{0} is palindrome".format(i))
    else:
        print("{0} is not palindrome".format(i))
