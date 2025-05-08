number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
multiplication = number1 * number2
print("The multiplication of two numbers is : ", multiplication)


from sys import argv

name = argv[1]
print(name, "is very good boy who helps everyone and also",name, "participates in all the sports and cultural meet.", name, "hobbies are playing virtual games and also watching movies.")


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = (base * height) / 2
print("The area of triangle is: ", area_triangle)


name = argv[1]
year = argv[2]
name_of_college = argv[3]
lives = argv[4]
print("student_name :", name)
print("class        :", year)
print("college_name :", name_of_college)
print("city_lives   :", lives)