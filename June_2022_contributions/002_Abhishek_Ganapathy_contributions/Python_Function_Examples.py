# Python function that accepts different values as parameters and returns a list

def myFruits(f1,f2,f3,f4):
    FruitsList = [f1,f2,f3,f4]
    return FruitsList
    
output = myFruits("Apple","Bannana","Grapes","Orange")
print(output)

# Python function that returns a dictionary
def myAnimals(a1,a2,a3):
    Animalgroup = {'Kitten':a1,'Puppy':a2,'Pup':a3}
    return Animalgroup

output = myAnimals("Cat","Dog","Rat")
print(output)

# Python function that returns a tuple

def myVeggies(v1,v2,v3):
    vegtuple = (v1,v2,v3)
    return vegtuple

output = myVeggies("Carrot","Potato","Tomato")
print(output)

# Python function that accepts a list as a parameter

def myChocolates(cList):
    for i in cList:
        print(i)

chocolateList = ["Dairy Milk","Snickers","Kitkat"]
myChocolates(chocolateList)

# Python function that accepts a dictionary as a parameter
def myVehicles(vDict):
        print(vDict)

vehicleDictionary = {
    'Tesla': 'Car',
    'Royal Enfield' : 'Bike'
    }
    
myVehicles(vehicleDictionary)

# Python function using positional arguments
def Car(name,model):
    print("Name:",name)
    print("Model:",model)
    
Car("Audi","Q7")

# Python function using keyword arguments
def Car(name,model):
    print("Name:",name)
    print("Model:",model)
    
Car(model="Q7",name="Audi")

# Python function using default arguments
def Car(name,model="Q7"):
    print(name)
    print(model)

def Car(name):
    print("The name of the car is",name)

Car("Audi")

def Car(name,model="Q7"):
    print("Name:",name)
    print("Model:",model)
    
Car("Audi","Q8")

# Python function using optional arguments
def Calendar(year,month,date=''):
    print(year,month,date)
    
Calendar(2023,2)

def Calendar(year,month,date=''):
    print(year,month,date)
    
Calendar(2023,2,14)

#  Passing an arbitrary number of arguments to a Python function
def Insects(*Insectslist):
    print(Insectslist)

Insects("Mosquito","Honeybee")

Insects("Mosquito","Honeybee","Beetles")

# Python function that returns multiple values

def SwapTwoNumbers(a,b):
    print("Before Swap: ",a,b)
    a = a+b
    b = a-b
    a = a-b
    return a,b
    
a,b = SwapTwoNumbers(17,24)
print("After Swap: ",a,b)

# Python function to check if a number is palindrome or not
def palindromeCheck(num):
    temp = num
    rev = 0
    while(num != 0):
        r = num%10
        rev = rev*10+r
        num = num//10
    if(rev == temp):
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")
    

palindromeCheck(131)
palindromeCheck(34)

# Python function to find the factorial of a number

def factorial(n):
    fact = 1
    while(n!=0):
        fact *= n 
        n = n-1
    print("The factorial is",fact)
    
inputNumber = int(input("Enter the number: "))
factorial(inputNumber)

# Python nested functions

def function1():
    p ="Hello Pythonista" 
    def function2():
        print(p)
    function2()
    
function1()