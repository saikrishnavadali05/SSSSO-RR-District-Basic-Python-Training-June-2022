#check whether given input is odd or even

number=int(input("Enter a Number:"))

if(number%2)==0:
    print("{0} is Even".format(number))
else:
    print("{0} is Odd".format(number))