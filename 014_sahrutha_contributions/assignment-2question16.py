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