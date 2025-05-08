#Write a script for factorial and take input from the command line parameter. using while and for loops

n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
    for i in range (1,int(n)+1):
        factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)