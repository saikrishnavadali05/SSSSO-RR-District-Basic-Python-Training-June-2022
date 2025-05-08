#Write a script for factorial and take input from the command line parameter. using while and for loops

number1 = int(input("enter the number n"))

i=number1
result = 1 
while (i>=1):
  result = result * (i)
  i = i -1 

print(result)

# same using for loop 

result1 = 1 
for i in range(1,number1+1):
    result1 = result1 * i 
print(result1)

#Write a script to print the count of number of digits within the given input number using while loop

count_digits = int(input("enter a number to count digits"))
counter = 0 
while (count_digits!=0):
    count_digits = count_digits//10
    counter = counter+1

print(counter)
 

