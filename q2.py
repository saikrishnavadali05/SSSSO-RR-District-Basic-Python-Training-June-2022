#2.	Write a program to find the maximum, minimum, average, 
# addition, multiplication of any 2 integer numbers (for example : 23 and 34)

# This program for adds two numbers

#num1=5
#num2=12

num1 = 5
num2 = 12
print ("print num1=",num1)
print ("print num2=",num2)
# Add two numbers
sum = num1 + num2

# Display the sum
print ("sum of two number =",sum)
#sum of two number = 17
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
#output=The sum of 5 and 12 is 17

# subtract two numbers
num1= 25
num2= 5
print ("print num1=",num1)
print ("print num2=",num2)

subtract = num1 - num2
# Display the subtraction of two number
print ("subtraction of two number =",subtract)
#output =subtraction of two number = -7

#NOW TAKE TWO INPUT FROM USER  
number1=int(input("enter number1:"))
number2=int(input("enter number2:"))
#enter number1:23
#enter number2:34
# find the maximum, minimum, average, 
# addition, multiplication of any 2 integer numbers 

# find the maximum of two number
print("maximum :",max(number1,number2))
#output =maximum : 34

# find the minimum of two number
print("find the minimum of two number")
print("minimum :",min(number1,number2))
#output =minimum : 23

# find the average of two number
print("find the average of two number")
print("average :",(number1+number2)/2)
#output= average : 28.5
print("addition :",(number1+number2))
#output=addition : 57

# find the multipication of two number
print("find the multipication of two number")
print("multipication :",(number1*number2)) 