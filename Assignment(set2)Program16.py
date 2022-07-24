#16.Create a function display_student_data() which takes student id, student name and marks as input. It should display all the data. If marks is missing it should display 75.
#Solution 1
class Student:
    
    def __init__(self, name):
        self.name = name
        self.id = id
         
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


#solution 2
n = 3
print("Enter in the following sequence")
print("Enter input as Identifier student id")
print("Enter input as Identifier student name") 
print("Enter input as Identifier marks")
Student_Data = dict(input("Enter key and value: ").split() for _ in range(n))
print(Student_Data)

for key,value in Student_Data.items():
    if value == '0':
        print("the key is",key)
        Student_Data[key] = 75
print(Student_Data)
