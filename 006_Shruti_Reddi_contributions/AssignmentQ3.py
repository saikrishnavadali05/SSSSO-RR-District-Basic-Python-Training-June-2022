#Write a program that accepts a positive integer n.
#  Next, write a function to find factorial of the number. 
# and next, write another function to compute the value of n+nn+nnn.
#  If n is 5, first output should be 5! = 120 and 
# the next output should be 5+55+555 = 615.

from audioop import add


num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")

def factorial(num):
      
    if num == 0:
        return 1
     
    return num * factorial(num-1)
print("Factorial of", num, "is",factorial(num)) 

def innu_add(num):
    add_sum =(num+(11*num)+(111*num))
    return add_sum

sum = innu_add(num)    
print("5+55+555=", sum)