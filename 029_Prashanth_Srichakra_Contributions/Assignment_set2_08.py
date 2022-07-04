# Write a program to check if the input string is a palindrome? Next, Make the program to work on integers as well. Write a palindrome function. Call that function of 5 different inputs to test whether the function is written properly or not.

def string_palindrome(string):
    rev_string = string[::-1]
    if rev_string == string:
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")

def number_palindrome(num):
    mod = 0
    rev = 0
    temp = num
    while num != 0:
        mod = num % 10
        rev = rev * 10 + mod
        num = num // 10

    if rev == temp:
        print(f"{temp} is a palindrome.")
    else:
        print(f"{temp} is not a palindrome.")


# Checking String
string = input("Enter a string: ")
string_palindrome(string)
print()

# Checking Numbers
number_palindrome(123)
number_palindrome(1221)
number_palindrome(999)
number_palindrome(100)
number_palindrome(6556)