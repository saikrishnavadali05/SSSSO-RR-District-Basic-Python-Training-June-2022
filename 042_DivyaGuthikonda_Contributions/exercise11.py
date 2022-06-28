# Given a list of numbers, write a Python program to find the sum of all the elements in the list.

Numbers=[22,23,5,4,16,8,7]
print("sum of elements in the list is ",sum(Numbers))
# sum of elements in the list is 85 

# Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User
print("Maximum number of list is ",max(Numbers))
print("Minimum Numbet of list is ",min(Numbers))
# Maximum number of list is 23
# Minimum number of list is 4

# inputs from user end
list=[]
len = int(input("Enter the length of elements "))
for i in range(len):
    elements=int(input("\nEnter elements of a list "))
    list.append(elements)
print("Maximum Number is ",max(list))
print("Minimum Number is ",min(list))
# output
'''
Enter the length of elements 5

Enter elements of a list 25

Enter elements of a list 65

Enter elements of a list 96

Enter elements of a list 756

Enter elements of a list 25
Maximum Number is  756
Minimum Number is  25
'''