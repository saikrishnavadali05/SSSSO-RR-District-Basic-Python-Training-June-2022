#Exercise 3
#Write the script asking the user to give two integers and multiply them.
from sys import argv

number1 = int(input("Enter first integer"))
number2 = int(input("Enter second integer"))
print("The result of ",number1, number2, "is:", number1 * number2)

name = argv[1]
para_text = name + "is very good boy who helps everyone and also " + name + "participates in all the sports and cultural meet. " + name + "hobbies are playing virtual games and also watching movies."
print(para_text)

#Write the script for calculating area of trainagle ( ask user to enter base and height).

number1 = float(input("Enter Base value"))
number2 = float(input("Enter Height value"))
print("The result of ",number1, number2, "is:", (number1 * number2)/2)

#Write the script of the student form(name_of_student, class_studying, college_name, city_lives) 
# that accepts as command line parameters and prints in specified format

student_name = argv[2]
class_value  = argv[3]
college_name = argv[4]
city_lives = argv[5]

print("student_name :",student_name," \n","Class :",class_value," \n","college_name :",college_name," \n","city_lives :",city_lives)
