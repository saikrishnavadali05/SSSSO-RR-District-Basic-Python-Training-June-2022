#count number of digits

number=int(input("Enter any number:"))
count=0
while (number>0):
    count=count+1
    number=number//10
print("The number of digits in given number is {0}".format(count))
