#create  *args  and  **kewargs used in "def" function:
#example:-1.
def calaculation(a,b):
    print("addition is:",a+b)      #addition is: 180
    print("subtraction is:",a-b)   #subtraction is: 60
    print("mutiplication is:",a*b) #mutiplication is: 7200
    print("division is:",a/b)      #division is: 2.0
calaculation(120,60)

def calaculation(a,b):
    print("addition is:",a+b)      #addition is: 1880 
    print("subtraction is:",a-b)   #subtraction is: 1120 
    print("mutiplication is:",a*b) #mutiplication is: 570000 
    print("division is:",a/b)      #division is: 3.9473684210526314
calaculation(1500,380)  

#create *args
def calaculation(*args):
    result=0
    for i in args:
        result+=i
    return result
print(calaculation(0))        #0
print(calaculation(6,70))     #76
print(calaculation(3,8,45))   #56   

def calaculation(*args):
    result=5
    for i in args:
        result+=i
    return result
print(calaculation(5))            #10
print(calaculation(10,70))        #85 
print(calaculation(3,45,45))      #98 
print(calaculation(45,39,70,23))  #182  

#Example:-2
def addition(a,b=8):  #a is positional , b is keyword:
    return a+b
print(addition(16))    #24

def calaculation(a,b,c=20):
    print(a+b+c)
calaculation(47,100)   #167       
def printer(a,b,*args):
    print(f'a is {a}')         # a is 100
    print(f'b is {b}')         # b is 500
    print(f'args is {args}')   # args is (5, 4, 7, 5)
printer(100,500,5,4,7,5)

def printer(a,b,c,d,*args):
    print(f'a is : {a}')             #a is : 69
    print(f'b is : {b}')             #b is : 75
    print(f'c is : {c}')             #c is : 634
    print(f'd is : {d}')             #d is : 82
    print(f'args is :{args}')        #args : (23,13,15)   
printer(69,75,634,82,23,13,15)          

'''#example:-3
def printer(a,b,*args):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"args is {args}")
printer(a=20,2,3,5,7)    #SyntaxError: positional argument follows keyword argument  '''

#Example:-4
def addition(a,b,*args,option=True):
    result=0
    if option:
        for i in args:
            result+=i
        return a+b+result
    else:
        return result
print(addition(1,2,2,6,3,6))               # 20
print(addition(1,2,2,6,3,6,option=False))  # 0  

def addition(a,b,*args,option=True):
    result=10
    if option:
        for i in args:
            result+=i
        return a+b+result
    else:
        return result
print(addition(1,2,2,6,3,6))               #30
print(addition(1,2,2,6,3,6,option=False))  #10   

#Example:-5:
def printer(a,b,option=False,**kwargs):
    print(a,",",b)     #93  , 34
    print(option)      #False
    print(kwargs)      #{'nunber': 5, 'age': 26}
printer(93,34,nunber=5,age=26)

def printer(a,b,option=True,**kwargs):
    print(a,",",b)           #100  , 39
    print(option)            #True
    print(kwargs)            #{'age1': 5, 'age2': 26}
printer(100,39,age1=5,age2=26)      

#Example:-6
def printer(a,b,*args,option=True,**kwargs):
    print(a,",",b)                 # 1000 , 236
    print(option)                  #True
    print(args)                    #(23, 23, 43, 52)
    print(kwargs)                 #{'marks': 98, 'id': 50, 'age': 23}
printer(1000,236,23,23,43,52,marks=98,id=50,age=23)

#Example:-7
def printer(*args):
    print(args)
lst=[2,6,8]
printer(lst)          #([2, 6, 8],)
printer(*lst)         #(2, 6, 8)       

def printer(*args):
    print(args)
tpl=(1,18,19)
printer(tpl)         #((1, 18, 19),)
printer(*tpl)        #(1, 18, 19)

#Example:-8
def printer(*args):
    print(args)         #(1, 7, 9, 10, 5, 7, 4, 18, 20)
lst=[1,7,9,10]
tpl=(5,7,4)
printer(*lst,*tpl,18,20)

#Example:-9
def printer(**kwargs):
    print(kwargs)                   #{'name': 'madhu', 'gender': 'male', 'id': '60'}
dct={"name":'madhu',"gender":'male',"id":'60'}
printer(**dct)

#Example:-10
def printer(**kwargs):
    print(kwargs)         #{'marks': 89, 'name': 'madhu', 'gender': 'male', 'id': '60'}
    print(dct)            #{'name': 'madhu', 'gender': 'male', 'id': '60'}
dct={"name":'madhu',"gender":'male',"id":'60'}
printer(marks=89,**dct)
