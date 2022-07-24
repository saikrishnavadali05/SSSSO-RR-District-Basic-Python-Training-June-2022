 #exercise 2

#Create a variable having the name: student_name and assign the value Ramesh to that newly created variable.

student_name = 'ramesh'
print(student_name)

#Given the problem to substract 5 from 10, using two variables with names: number1 and number2 and store the final result in number3.Print the final output.

number1 = 10
number2 = 5
number3 = number1 - number2
print(number3)

#Write a script that defines and uses the following variables for writing a meaningful english line

colour = "blue"
fruit = "Mango"
number = 22
article = "is"

#use the variables above to print the following statements exactly

print("sky", article, colour  +"," , fruit, article, "yellow, age of suresh",  article, number , ".")

#practice of the similar eample

name = "chandhini"
age = 22
qualification = "msc"
av = 'is'
print("I am", name  +"," , "years old", av, age , "my education", av, qualification , ".")

    # user input

MyName = input("what is my name : " )
print("my name is : ", MyName)
number_of_words = input("number of words :")
print("enter number of words:" , number_of_words)
print(type(MyName))
print(type(number_of_words))


number_of_words = int(number_of_words)
print(number_of_words)
print(type(number_of_words))
 
 # exercise 3


#Write the script asking the user to give two integers and multiply them.


first_event = int(input(" enter first number"))  # here the type of datatype is specified by the user
second_event = int(input("enter second nuber"))
print("first number is:" , first_event)
print("second number is:" , second_event)
multiply = first_event * second_event
print(multiply)


#Write the script for calculating area of trainagle ( ask user to enter base and height).


base_dimension = float(input("enter the base value"))
height_dimension = float(input(" enter the height value"))
area = (1/2) * base_dimension * height_dimension
print(area)
print(type(area))
