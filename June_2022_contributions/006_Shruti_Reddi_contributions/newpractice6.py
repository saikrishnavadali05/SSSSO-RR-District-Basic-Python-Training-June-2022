# call function with 3 arguments
#func1(20, 40, 60)

# call function with 2 arguments
#func1(80, 100)

#def call_arguments(x,y,z):
   # print(x)
    #print(y)
    #print(z)

#call_arguments(20,40,60)

#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

#def calculation(x,y):
   # a=x+y
   # b=x-y
    #return a, b
#res = calculation(100,200)
#print(res)

#Write a program to create a function show_employee() using the following conditions.

#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign
#  default value 9000 to salary
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa", 5000)
 