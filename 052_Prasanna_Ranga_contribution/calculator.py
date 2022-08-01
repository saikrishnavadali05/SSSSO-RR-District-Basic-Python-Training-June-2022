# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2


# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2


print("Please select operation -\n" \
		"1. Add\n" \
		"2. Multiply\n" )
		


# Take input from the user
select = int(input("Select operations form 1, 2 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))



elif select == 2:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))


else:
	print("Invalid input")
