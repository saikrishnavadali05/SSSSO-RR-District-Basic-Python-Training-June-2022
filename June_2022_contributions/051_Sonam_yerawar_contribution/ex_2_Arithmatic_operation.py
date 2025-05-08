#Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)




from statistics import mean


print("This program is for finding max,min,avg,addition,mult")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
list1=[num1,num2]
print("maximum number is: ",max(num1,num2))
print("minimum number is: ",min(num1,num2))
y=mean(list1)
print("average is: ",y)
print("addition is: ",num1+num2)
print("multiplication is :",num1*num2)
