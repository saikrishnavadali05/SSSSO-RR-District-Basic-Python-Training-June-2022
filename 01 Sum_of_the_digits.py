# Write a program to print the sum of the digits. For example if the input is 123, the result should be 6.
# # Method 1 using the while loop logic 
number = int(input("Enter the digits here:"))
sum = 0
while number > 0:
    rem = number % 10
    sum += rem 
    number //= 10
print("The sum of the given digits is ",sum)

# # Method 2 using the for loop 

number1 = int(input("Enter the number here:"))
sum1 = 0
for i in str(number1):
    sum1 += int(i)
print("The sum of the given digits is",sum1)

