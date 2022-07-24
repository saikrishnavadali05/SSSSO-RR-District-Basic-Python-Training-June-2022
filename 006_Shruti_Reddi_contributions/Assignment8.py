#Write a program to check if the input string is a palindrome?
#  Next, Make the program to work on integers as well. 
# Write a palindrome function. 
# Call that function of 5 different inputs to test 
# whether the function is written properly or not.


# using str() + string slicing
# for checking a string is palindrome
a_string = input("Enter a String :")
def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]
print(palindrome(a_string))


# using str() + string slicing
# for checking a string is palindrome
a_number = input("Enter numbers: ")
def palindrome(number):
    number = str(number)
    return number == number[::-1]
print(palindrome(a_number))
# Returns: True
