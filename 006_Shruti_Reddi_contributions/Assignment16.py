class Student:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.id = id
        
    
         
    # Function to create and append new student   
    def enterMarks(self):
            m = int(input("Enter the marks:"))
            self.marks=m

    def display(self):
        print (self.name, "with ID No", self.id ,"got marks", self.marks)

name = input("Enter the name of Student:")
id = input("Enter the ID of the student:")
s1 = Student(name)
s1.enterMarks()
s1.display()

name = input("Enter the name of Student:")
id = input("Enter the ID of the student:")
s2 = Student(name)
s2.enterMarks()
s2.display()