#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (give input numbers)

num1=input("Enter Number 1")
num2=input("Enter Number 2")

#defining Maximum and minimum using formula

maximum=((int(num1)+int(num2)+abs(int(num1)-int(num2)))//2)
print('The maximum  =', maximum)

minimum=((int(num1)+int(num2)-abs(int(num1)-int(num2)))//2)
print('The minimum =', minimum)

#defining average of the given numbers
average=(int(num1)+int(num2))/2
print('The average =', average)

#defining addition and multiplication of the given numbers

addition= int(num1)+int(num2)
print('The addition  =', addition)

multiplication=int(num1)*int(num2)
print('The multiplication  =', multiplication)