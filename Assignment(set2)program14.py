#14.Write a function add which takes variable parameters using *args and **kwargs. and it returns the sum of all arguments which are integers (hint : research about *args and **kwargs in python on google).
def myGod(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3) 
args = ("Jai", "Sai", "Ram")
myGod(*args) 
kwargs = {"arg1": "Welcome", "arg2": "to", "arg3": "world"}
myGod(**kwargs)

def myLife(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
myLife('Respect', 'for', 'all', first="All", mid="Are", last="Equal")

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))