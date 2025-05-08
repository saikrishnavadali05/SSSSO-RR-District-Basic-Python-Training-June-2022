import add as a
import multiply as m

print("Calulator for Addition and Multiplication") 
operation = input("Enter operation add or multiply: ")
if operation == "add":
    a.add()
elif operation == "multiply":
    m.multiply()
else:
    print("Please enter a valid operation!")
