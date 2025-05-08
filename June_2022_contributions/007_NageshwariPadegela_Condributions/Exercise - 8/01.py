# Write a script for factorial and take input from the command line parameter. using while and for loops
'''
For example, factorial of 4! is 4 * 3 * 2 * 1 = 24.
Input of your code should take n as input.
Output of your code should be n!
'''
num = int(input('Enter a number to whixh you need to find the factorial: '))
if num<0:
    print("There is no factorial for the number %d"%num)
else: 
    product = 1
    for i in range(1, num+1, 1):
        product = i*product
    print("Factorial of a %d is %d"%(num, product))


     
