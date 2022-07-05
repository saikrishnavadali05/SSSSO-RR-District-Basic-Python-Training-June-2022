#parameters in python:
'''def name(a):
    return(a)
a=name("WELCOME TO PYTHON LIFE")
print(a)
def add(a,b,c,d=50):
    return(a+b+c+d)
e=add("WELCOME", "TO", "PYTHONLIFE","50")
print(e)  
def add(a,b,c):
    return(a+b+c)
d=add(50,65,45)
print(d)
def add(a,b=99,c=84):
    return(a+b+c)
d=add(50)
print(d)
def nested_list_demo():
    value=["m","n",13,14]
    value[0:1]=[20,25]
    print(value)     #[20, 25, 'n', 13, 14]
    value[1:3]=[]
    print(value)
    print("lenth of the value is:",len(value))
    print(type(value))
    #neasting of lists
    a=[10,20,30,40]
    b=[5,a,25]
    print(b)
    print(b,b[1])
    a=[1,2,3,4]
    b=[a,5,a]
    print(b)
    print(b,b[1])
    a.sort()
    print(a)
    b[2].append(10)
    print(b)
nested_list_demo()
print()
def nested_list_demo():
    var=["m",'n','o',15,20,25]
    print(var)
    var[2:4]=[16,30]
    print(var)
    var[2:6]=[]
    print(var)
    print("enter the lenth of var is:",len(var))
    print(type(var[2:4]))
    #nested values:
    a=[9,8,7,6]
    b=[5,a,3,a]
    print(b)
    print(a,b[-1])
    a.sort()
    print(a)
    b.append(30)
    print(b)
    
nested_list_demo()
print()
#creat the conditional statement
name="GOWTHAM"
range=name
for i in range :
    print(i)  
a=("gowthamreddy")
b=a[3:10]
range=b 
for i in range:
    print(i)  

#function:1
def square(a):
   return a*a
print(square.__doc__)
def square(b=8):
   return 8*8
print(square(8))



def deference(a,b):
    return(a-b)
print(deference.__doc__)

deference();
print()

#create functions:
#1.first def funtion:
def evenOrOdd(numbers):
    if (numbers%2==0):
        print('{} is even'.format(numbers))
    else:
        print('{}is odd'.format(numbers))


print("evenOrOdd",13,"\n","evenOrOdd",65,"\n","evenOrOdd",90,"\n","evenOrOdd",35,"\n","evenOrOdd",27,"\n","evenOrOdd",48)
evenOrOdd(13)
evenOrOdd(65)
evenOrOdd(90)
evenOrOdd(35)
evenOrOdd(27)
evenOrOdd(48)
print()             
def addition_two_values(value1,value2):
    addition=value1+value2
    return addition
result=addition_two_values(652,505)
print('enter the add value is:',result)        #enter the add value is: 1157

def deference_two_values(value1,value2):
    deference=value1-value2
    return deference
result=deference_two_values(652,505)
print('enter the deference value is:',result) #enter the deference value is: 147     

def multiplay(*args):
    mult=1
    for number in args: 
        mult= mult*number
    return mult 
result=multiplay(1,2,3,4,5)
print(result)                      #12o

def multiplay(*args):
    mult=2
    for number in args: 
        mult= mult*number
    return mult 
result=multiplay(1,7,8,9,10,5,6)
print(result)                       #302400        '''
#  exicise 10
#1.Write a function that take string as a parameter. the string is given by the user as input. the final output from the function is to reverse the string.
# example the string is Multiple - output is elpitluM
'''var="multiple"
for i in var:
    print(i)
name=str(input("enter the name is:"))
print(name)
b=var[::-1]
print(b) '''
def variableString(reverse*args) :
    string="multiple"
    for i in *args:
        string=i+reverse*args
    return string 
string=input("enter the string ")
result=variableString(multiple)
print("enter the reverse string",result)
























