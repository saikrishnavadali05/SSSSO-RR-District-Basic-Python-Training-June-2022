"""
1. Write a program to build a calculator. 
The calculator should be able to read 4 numbers and print the addition 
and multiplication of ONLY THE EVEN numbers using functions. You can follow these steps -

	a) Create different python files - add.py, multiple.py and 
    write functions for these operations.
	b) main.py file should call the above functions based on the inputs provided. 
    For example, input 'add 1,2,3,4'  should call add.py 
	'multiply 1,2,3,4'  should call multiply.py
	c) If there are less than 4 numbers provided, the code should 
    be able to handle the error and throw relevant message to the user.
	d) All the 4 numbers should be taken up with input() method.
	e) If no even number is there among the 4 numbers, it should throw 
    relevant message to the user.
	f) Save the program output into a text file output.txt
"""
from add import addition
from multiple import mul
input_user = input("Enter the four numbers: ")

try:
    lst = []
    if  len(input_user) == 4:
        a = input_user
        for i in a:
            if int(i)%2 == 0:
                lst.append(i)
    if len(lst) < 4:
        print("please given the even numbers only")
    else:
        print("The addition of given even numbers is ",addition(lst))
        print("The multiplication of given even numbers is",mul(lst))


    
except:
    print("please enter the limited numbers as input")

