# Write a script to print the count of number of digits within the given input number using while loop
'''
input from the user is 123.
number of digits in the above number are 3.
Hence the output count should return 3.
'''

number = int(input("Enter a number of your choice: "))
count = 0
while number >0:
    count += 1
    number = number//10
print('Number of digits are: ',count)
