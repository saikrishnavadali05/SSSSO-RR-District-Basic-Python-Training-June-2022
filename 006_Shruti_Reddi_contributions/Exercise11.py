#Exercise-11
#Given a list of numbers, write a Python program to find the sum of all the elements in the list.
list = [1,2,3,4,5,6,7,8,9]
sum_numbers = sum(list)
print('The sum of all elements of the list is:',sum_numbers )

#Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User

def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)