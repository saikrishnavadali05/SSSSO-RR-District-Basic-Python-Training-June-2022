"""
14.Write a function add which takes variable parameters using *args and **kwargs. 
and it returns the sum of all arguments which are integers 
(hint : research about *args and **kwargs in python on google).
"""
def add(*num):
    s = 0

    for i in num:
        s+= i
    return "The sum is  "+ str(s)
print("The args will take the multiple arguments and it will do the operations of funtion")
print(add(3,5,6))
print("-----------------------------------------------------------")
def fun(**num):
    print(type(num))
    for k, v in num.items():
        print(k,v)
    return ""
print("The kwarg will act as a dictionary")
print(fun(a=3,b=5,c=6))