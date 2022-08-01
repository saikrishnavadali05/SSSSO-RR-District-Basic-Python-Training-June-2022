# 3. Write a program that accepts a positive integer n. Next, write a function to find factorial of the number.
#  and next, write another function to compute the value of n+nn+nnn. If n is 5, first output should be 5! = 120 
# and the next output should be 5+55+555 = 615.
def fact(n):
    fact = 1
    while n != 0:
        fact *= n
        n = n-1
    return fact

num = input("Enter any positive integer:")
n = int(num)
factorial = fact(n)
print("The factorial of {0} is {1}".format(n, factorial))
n1 = num
n2 = num*2
n3 = num*3
result = int(n1)+int(n2)+int(n3)
print("{0}+{1}+{2}={3}".format(n1, n2, n3, result))