#Write a program that accepts a positive integer n. Next, write a function to find factorial of the number. 
#and next, write another function to compute the value of n+nn+nnn. If n is 5, first output should be 5! = 120 and 
#the next output should be 5+55+555 = 615.
num = int(input("Enter a number: "))    
fact = 1  
sum = num 
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       fact = fact*i    
   print("The factorial of",num,"is",fact)
      
sum = (num * 1) + (num * 11) + (num * 111)
print("The the computed value of",sum)