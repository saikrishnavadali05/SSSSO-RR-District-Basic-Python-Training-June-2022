# Given a list of numbers, write a Python program to find the sum of all the elements in the list.
Number_List = list(input("Enter the list "))
Length_of_the_list = len(Number_List)
Sum = 0
print("The length of the list is:",Length_of_the_list)
for i in range(0,Length_of_the_list):
    Sum = Sum + int(Number_List[i])
    i = i + 1
print("The sum of the numbers in the list",Number_List, "is:",Sum)

# Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User

Comparison_list = list(input("Enter the list which needs to be compared "))
Length_of_the_list2 = len(Comparison_list)
Largest = 0
Smallest = 0
for i in range(0,Length_of_the_list2):
    if(Comparison_list[i] < Comparison_list[Length_of_the_list2-1]):
        Smallest = Comparison_list[i]
    else:
        Largest = Comparison_list[i]    
print("The Smallest number in the list is", Smallest)
print("The Largest number in the list is", Largest)