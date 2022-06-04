"""
Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 1245, the output shall be “5 4 2 1“, with a space separating the digits.

"""


#solution
number = 1245
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")