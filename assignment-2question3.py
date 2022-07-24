def fact(num):
    fact = 1
    while num != 0:
        fact *= num
        num = num-1
    return fact


# inpput from user
number = input("Enter any positive integer:")
num = int(number)
# calling factorial function
factorial = fact(num)
print("The factorial of {0} is {1}".format(num, factorial))
# n+nn+nnn
num1 = number
num2 = number*2
num3 = number*3
result = int(num1)+int(num2)+int(num3)
print("{0}+{1}+{2}={3}".format(num1, num2, num3, result))