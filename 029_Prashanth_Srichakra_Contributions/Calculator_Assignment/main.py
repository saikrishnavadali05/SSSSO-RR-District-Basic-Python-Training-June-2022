import add as a
import mul as m

print("Welcome to Calculator!!!")
operation = input("Enter operation: ")
if operation == "add":
    a.add()
elif operation == "multiply":
    m.mul()
else:
    print("Please enter a valid operation!")
