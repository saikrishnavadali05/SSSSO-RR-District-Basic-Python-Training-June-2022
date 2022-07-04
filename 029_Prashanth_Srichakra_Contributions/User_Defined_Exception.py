# Creating a user defined Exception class that inherits Exception class

class MyException(Exception):
    def __init__(self):
        self.msg = "Division By Zero Is Not Possible!"

# Driver Code
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if(b == 0):
        raise MyException # Explicitly raising MyException
    c = a / b
    print("a / b =", c)

except MyException as e:
    print(e.msg)
