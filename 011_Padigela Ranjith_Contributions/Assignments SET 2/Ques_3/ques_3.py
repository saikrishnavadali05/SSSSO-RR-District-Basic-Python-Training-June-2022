"""
Write a program that accepts a positive integer n. 
Next, write a function to find factorial of the number. 
and next, write another function to compute the value of n+nn+nnn. 
If n is 5, first output should be 5! = 120 and the next output should be 5+55+555 = 615.

"""
n = int(input("Enter the number here: "))
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def compute(n):
    i = str(n)
    x = i
    y = i + i
    z = i + i + i
    return int(x) + int(y) + int(z)

print("This is first output {0}! =".format(n),factorial(n))
print("This is Second output {0}+{0}{0}+{0}{0}{0} =".format(n),compute(n))

