# Write a program to print the add, subtract, divide, multiply, of the digits using functions. Add, subtract, divide, multiply functions should be created. For example, if the input is 235, the result should be 10. Next, Load the input number 235 from a text file input.txt. Next, Save the program output into a text file output.txt.

# All the function's defnitions are written using non-conventional logic

def add(a):
    sum = 0
    for i in a:
        sum += int(i)
    return str(sum)

def sub(a):
    diff = int(a[0])
    i = 1
    while i < len(a):
        diff = diff - int(a[i])
        i = i + 1
    return str(diff)

def mul(a):
    product = 1
    for i in a:
        product *= int(i)
    return str(product)

def div(a):
    quotient = int(a[0])
    i = 1
    while i < len(a):
        quotient = quotient / int(a[i])
        i += 1
    return str(quotient)

# Opening Input File
input_file = open("input.txt", 'r')

# Reading Input Number
num = input_file.read()

# Closing File
input_file.close()

# Writing Outputs into Output File
output_file = open("output.txt", 'w')
add_result = 'Sum of digits is: ' + add(num)
sub_result = 'Differnece of digits is: ' + sub(num)
mul_result = 'Product of digits is: ' + mul(num)
div_result = 'Quotient after dividing consecutive digits is: ' + div(num)
output_file.write(f'The input number is : {num}\n')
output_file.writelines([add_result,'\n', sub_result,'\n', mul_result,'\n', div_result])
output_file.close()

# File Contents

# input.txt
# 235

# output.txt    
# The input number is : 235
# Sum of digits is: 10
# Differnece of digits is: -6
# Product of digits is: 30
# Quotient after dividing consecutive digits is: 0.13333333333333333