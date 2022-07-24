#Assignments (SET-2)
#1.Write a program to print the add, subtract, divide, multiply, of the digits using functions. Add, subtract, divide, multiply functions should be created. For example, if the input is 235, the result should be 10. Next, Load the input number 235 from a text file input.txt. Next, Save the program output into a text file output.txt.
a=888
b=500
result=10
def add(x,y):
    print("addition is:",x+y)      #(file2.txt)addition is: 257
def sub(x,y):
    print("subtraction is:",x-y)   #(file2.txt) subtraction is: 10
def mul(x,y):
    print("multiplication is:",x*y) #(file2.txt) multiplication is: 14950
def div(x,y):
    print("division is:",x/y)       #(file2.txt) division is: 65.0  
import file3
file3.add(235,22)
file3.sub(235,225)
file3.mul(230,65)
file3.div(260,4) 
#2.Given a Full name stored in a input file input_name.txt which contains first name, middle name and last name. All the first, middle and last name are seperated by spaces. Print the output in the following order: Last Name, First Name, middle name. Next, Save the last name in last_name.txt file. Save the first name in first_name.txt. Save the middle name in middle_name.txt file.
names=str(input("enter the  names:"))  #enter the  names:MAHENDRA RAO PALAKOLLA
names=names.split()
if len(names)==3:
  fname,mname,lname=names
else:
  fname=names[0]       #First_Name : MAHENDRA
  mname=names[1]       #Middle_Name : RAO
  lname=names[2]       #Last_Name : PALAKOLLA  
print("\n","First_Name :",fname,"\n","Middle_Name :",mname,"\n","Last_Name :",lname)
import file3
file3.fname
file3.lname
file3.mname 
  
#3.Write a program that accepts a positive integer n. Next, write a function to find factorial of the number. and next, write another function to compute the value of n+nn+nnn. If n is 5, first output should be 5! = 120 and the next output should be 5+55+555 = 615.
factorial=1
n=5
for i in range(1,n+1):
  factorial=factorial*i
print("{}!={}".format(n,factorial))   #5!=120
#          (or)
def factorial(n):
  return 1 if (n==1 or n==0) else n*factorial(n-1)
n=5
print(factorial(n))       #120
n=5
a=int("%s" % n)
b=int("%s%s" % (n,n))
c=int("%s%s%s" % (n,n,n))
d=a+b+c
print(n,"+",n,n,"+",n,n,n,"=",d)   #5 + 5 5 + 5 5 5 = 615    

#4.Write a program to load, open and save an image. (hint : use opencv-python or PIL modules. Research about them on google and youtube)

#5.Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. Accept from the user the count of numbers and the actual numbers.
num=[3,4,5,6,7,8,9,15,31]
even_sum=0
odd_sum=0
for i in range(len(num)):
  if num[i]%2==0:
    even_sum=even_sum+num[i]
  else:
    odd_sum=odd_sum+num[i]
print("sum of even number:",even_sum)    #sum of even number: 18
print("sum of odd number:",odd_sum)     #sum of odd number: 70      

#6.Find out what is a timestamp? Print date and time in a timestamp. Print the seconds, hours, minutes as sepearate integer numbers from that timestamp. (hint : use datetime module. Search on google when stuck).
import pandas as pd
import numpy as np
print('pandas:',pd.__version__)
print('numpy:',np.__version__)
x=pd.timestamp('2022-07-21 22:37:50')
print(x)      

#7.Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.
s=("mahendra")
print("enter the upper case:",s.upper())    #enter the upper case: MAHENDRA
s1=("FALSE")
print("enter the lower case:",s1.lower())   #enter the lower case: false
a=s
b=s1
for i in range(len(a)):
  print(i)               #0  1  2  3  4  5  6  7
for j in range(len(b)):
  print(j)              #0  1  2  3  4       

#8.Write a program to check if the input string is a palindrome? Next, Make the program to work on integers as well. Write a palindrome function. Call that function of 5 different inputs to test whether the function is written properly or not.
#9.Store student name, id, age, class, course in a dictionary. Write a script to lookup a student name, age, class, course given the student ids.
student={"Name":'Chandu',"Age":'23',"class":'Degree',"Course":'B.sc',"Id":'50'}
print(student)
d=student
print("enter student values:",d.values())
#enter student values: dict_values(['Chandu', '23', 'Degree', 'B.sc', '50'])
print("items:",d.items())
#items: dict_items([('Name', 'Chandu'), ('Age', '23'), ('class', 'Degree'), ('Course', 'B.sc'), ('Id', '50')])


