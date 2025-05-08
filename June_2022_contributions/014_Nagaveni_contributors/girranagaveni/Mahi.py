#parameters in python:
def name(a):
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