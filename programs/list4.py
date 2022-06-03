"""

Given a list of numbers, the task is to write a Python program to find the largest number in given list.

Examples:

Input : list1 = [10, 20, 4]
Output : 20

"""

#solution

# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])
