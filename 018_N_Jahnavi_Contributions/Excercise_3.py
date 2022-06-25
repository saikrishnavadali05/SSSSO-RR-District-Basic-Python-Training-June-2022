# Q.1: Write the script asking the user to give two integers and multiply them.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
product = num1 * num2 
print("The product of num1 and num2 is ", product)

# Q.2 use command line prompt, take input any name (Girish is used here) and print the given paragraph.
# Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.
from sys import argv

name = argv[1]

print(name, "is very good boy who helps everyone and also", name, "participates in all the sports and cultural meet.", name, "hobbies are playing virtual games and also watching movies.")
print("\t")

# Q.3 : Program to calculate the area of trainagle ( ask user to enter base and height).

height = int(input("Enter height: "))
base = int(input("Enter base: "))
Area = 1/2 * (height * base) 
print("The area  of triangle is ", Area)

# Q.4: Command line parameters to print details of student

from sys import argv

name_of_student = argv[1]
class_studying = argv[2]
college_name = argv[3]
city_lives = argv[4]

print("student_name : ", name_of_student)
print("class : ",  class_studying)
print("college_name : ", college_name)
print("city_lives : ", city_lives)

