1. Write a program to build a calculator. The calculator should be able to read 4 numbers and print the addition and multiplication of ONLY THE EVEN numbers using functions. You can follow these steps -
	a) Create different python files - add.py, multiple.py and write functions for these operations.
	b) main.py file should call the above functions based on the inputs provided. For example, input 'add 1,2,3,4'  should call add.py 
	'multiply 1,2,3,4'  should call multiply.py
	c) If there are less than 4 numbers provided, the code should be able to handle the error and throw relevant message to the user.
	d) All the 4 numbers should be taken up with input() method.
	e) If no even number is there among the 4 numbers, it should throw relevant message to the user.
	f) Save the program output into a text file output.txt  
a=25
b=34
c=38
d=50
def calculator(a,b,c,d):
    return a+b+c+d
    
result=a+b+c+d
print("addition :",calculator(a,b,c,d))   # addition : 1503

def multiple(a,b,c,d):
    return a*b*c*d
    
result=a*b*c*d
print("multiple :",multiple(a,b,c,d))  #multiple : 17433292888  

a=888
b=500
c=485
d=344
result=10
def add(m,n,o,p):
    print("addition is:",m+n+o+p)      
    import Exam
Exam.add(25,45,56,34)       #  addition is: 160  
def mul(m,n,o,p):
    print("multiplication is:",m*n*o*p)
    import Exam 
Exam.mul(23,30,45,62)       #multiplication is: 1925100






