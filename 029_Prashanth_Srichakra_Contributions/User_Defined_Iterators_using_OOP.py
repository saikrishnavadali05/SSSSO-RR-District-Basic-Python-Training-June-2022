# Create a class containing __init__(), __iter__() and __next__() methods and define them as per need.

class myclass:
    def __init__(self,*x):
        self.list_items = x

    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        x = self.list_items[self.a]
        self.a += 1
        return x

# Creating an object for myclass
obj = myclass('apple','banana','kiwi')

# Creating an iterator for obj
myit = iter(obj)

# Iterating using next()
print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # kiwi