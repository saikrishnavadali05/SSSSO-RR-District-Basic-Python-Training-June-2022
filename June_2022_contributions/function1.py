#14.Write a function add which takes variable parameters using *args and **kwargs. and it returns the sum of all arguments which are integers (hint : research about *args and **kwargs in python on google).
def addition(a,b,*args,option=True):
    result=0
    if option:
        for i in args:
            result+=i
        return a+b+result
    else:
        return result    
print("sum of all arguments:",addition(1500,500,20,50,89))              #sum of all arguments: 2159
print("sum of all arguments:",addition(1500,500,20,50,89,option=False)) #sum of all arguments: 0  

def printer(a,b,*args,option=True,**kwargs):
    print(f'a is :{a}')               #  a is :34
    print(f'b is :{b}')               #  b is :36
    print(f'args is:{args}')          #  args is:(75, 69, 79)
    print(f'option is :{option}' )    #  option is :True
    print(f'kwargs is :{kwargs}')     #  kwargs is :{'name': 1, 'age': 7}
printer(34,36,75,69,79,name=1,age=7)  

#15.Write a function calculate() such that it can accept two variables and calculate the addition, multiplication of them. The result must be returned a single return call. The two variables are lists. (Do arithmetic operations on lists).
a=[1,6,8]
b=[9,4,7]
def calculate(add,*args):
    return a+b
lst=a+b
print("addition:",calculate(*lst))       # addition:[1, 6, 8, 9, 4, 7]

def calculate(a,b,*args):
    return a*b
print("mutiplication:",calculate(*[2],*[3]))   #mutiplication: 6  

#16.Create a function display_student_data() which takes student id, student name and marks as input. It should display all the data. If marks is missing it should display 75.
def printer(**kwargs):
    print(kwargs)                 #{'marks': 75, 's_name': 'mahi', 's_id': '50'}
dct={"s_name":'mahi',"s_id":'50'}
printer(marks=75,**dct)         



