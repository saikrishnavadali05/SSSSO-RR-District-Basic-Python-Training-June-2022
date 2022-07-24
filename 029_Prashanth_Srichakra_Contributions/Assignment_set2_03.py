# Write a program that accepts a positive integer n. Next, write a function to find factorial of the number. and next, write another function to compute the value of n+nn+nnn. If n is 5, first output should be 5! = 120 and the next output should be 5+55+555 = 615.

def fact(a):
    fact = 1
    i = 1
    if a == 0 or a == 1:
        return a
    while i <= a:
        fact *= i
        i += 1
    return fact

def series(n):
    result = n+(11*n)+(111*n)
    return result

# Reading number from user
num = int(input("Enter a number: "))
num_fact = fact(num)
num_series = series(num)

# Printing Outputs
print(f'{num}! = {num_fact}')
print(f'{num}+{11*num}+{111*num} = {num_series}')
        