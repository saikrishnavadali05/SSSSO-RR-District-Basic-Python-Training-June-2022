# Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. Accept from the user the count of numbers and the actual numbers.

list =[]
n = int(input("Enter size of list: "))

for i in range(0,n):
    element = int(input(f"Enter element {i}: "))
    list.append(element)

even_elements_sum = 0
odd_elements_sum = 0

for i in range(0,n):
    if list[i] % 2 == 0:
        even_elements_sum += list[i]
    elif list[i] % 2 != 0:
        odd_elements_sum += list[i]

print('Given List is', list)
print('Sum of all the even elements in given list is', even_elements_sum)
print('Sum of all the odd elements in given list is', odd_elements_sum)