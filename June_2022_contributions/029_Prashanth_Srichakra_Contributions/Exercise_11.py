# Exercise-11
# Given a list of numbers, write a Python program to find the sum of all the elements in the list.
numbers = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in numbers:
    sum += i
print("Sum of all the elements in the list is", sum)

#Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User
list_items = list(input("Enter list elements: "))
print("Smallest item in given list is ", min(list_items))
print("Largest item in given list is ", max(list_items))