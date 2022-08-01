#1.Write a program to print the add, subtract, divide, multiply, of the digits using functions. Add, subtract, divide, multiply functions should be created. For example, if the input is 235, the result should be 10. Next, Load the input number 235 from a text file input.txt. Next, Save the program output into a text file output.txt.
def add(num):
    sum = 0
    while num:
        r = int(num % 10)
        sum += r  # 123=1+2+3
        num = int(num/10)
    return sum
def subtract(num):
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    difference = lst[-1]
    for i in lst[:-1]:
        difference -= i  
    return difference
def multiply(num):
    product = 1
    while num:
        product = product*int(num % 10)  
        num = int(num/10)
    return product
def divide(num):    
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    divide = lst[-1]
    for i in lst[:-1]:
        divide /= i  
    return divide
with open(r"C:\Users\UDAY\Desktop\inital.txt", 'r') as f:
    n = f.read()
num = int(n)
sum = add(num)
difference = subtract(num)
product = multiply(num)
result = divide(num)
lines = {"sum": sum, "difference": difference,
         "product": product, "division result": result}
string = str(lines)
with open(r"C:\Users\UDAY\Desktop\output.txt", "w") as f:
    f.write(string)