#Exercise - 3
#Write the script asking the user to give two integers and multiply them.
#a= input("Enter Number 1 ")
#b= input("Enter number 2 ")
#c=int(a)*int(b)
#print(int(c)) #output Enter Number 1 45 Enter number 2 65 2925
#Take the command line parameter any name you want (C:> C:\Users\Documents\Training\code> python command_line_parameter.py Girish and print in the following paragraph.
#from sys import argv

#name = argv[1]

#print(name, "is very good boy who helps everyone and also",name, "participates in all the sports and cultural meet.", name, "hobbies are playing virtual games and also watching movies.")
#Output Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.

#Write the script for calculating area of trainagle ( ask user to enter base and height).
#base = input("Enter base")
#height = input("Enter height")
#area_of_triangle= 0.5*int(base)*int(height)
#print("The area of triangle is :",area_of_triangle )
#Enter base 12 #Enter height 15 #The area of triangle is : 90.0

#Write the script of the student form(name_of_student, class_studying, college_name, city_lives) that accepts as command line parameters and prints as
 
    #from sys import argv
    #print("argv list : ", argv)
    #student_name = argv[1]
    #class  = argv[2]
    #college_name = argv[3]
    #city_lives   = argv[4]
    #print("student_name :", student_name)
    #print("class :", class)
    #print("college_name :", college_name)
    #print("city_lives :", city_lives)

from sys import argv

print("argv list : ", argv)
student_name = argv[1]
classe = argv[2]
college_name = argv[3]
city_lives = argv[4]
print("student_name :", student_name)
print("class :", classe)
print("college_name :", college_name)
print("city_lives :", city_lives)

# Output
#student_name : Hareesh Sai
#class : 12th
#college_name : SSB
#city_lives : Hyderabad