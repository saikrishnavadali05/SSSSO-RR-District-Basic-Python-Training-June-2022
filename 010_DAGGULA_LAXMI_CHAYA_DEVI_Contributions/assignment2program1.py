# Write a program to print the add, subtract, divide, multiply, of the digits using functions. Add, subtract, divide, multiply functions should be created. For example, if the input is 235, the result should be 10. Next, Load the input number 235 from a text file input.txt. Next, Save the program output into a text file output.txt.

# addition of digits of a number
def add(num):
    sum = 0
    while num:
        r = int(num % 10)
        sum += r  # 123=1+2+3
        num = int(num/10)
    return sum

# difference of digits in a number


def subtract(num):
    # initializing list
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    difference = lst[-1]
    for i in lst[:-1]:
        difference -= i  # 123=1-2-3
    return difference

# multiply digits of a number function


def multiply(num):
    product = 1
    while num:
        product = product*int(num % 10)  # 123=1*2*3
        num = int(num/10)
    return product

# divide digits of a num


def divide(num):
    # initializing list
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    divide = lst[-1]
    for i in lst[:-1]:
        divide /= i  # 123=1/2/3
    return divide


# taking input from a input.txt file
with open("input.txt", 'r') as f:
    n = f.read()
num = int(n)
sum = add(num)
difference = subtract(num)
product = multiply(num)
result = divide(num)
lines = {"sum": sum, "difference": difference,
         "product": product, "division result": result}
string = str(lines)

# printing output in output.txt file
with open("output.txt", "w") as f:
    f.write(string)
