#5.Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. Accept from the user the count of numbers and the actual numbers.
list = []
n = int(input("Enter number of elements in list is "))
for i in range(n):
    num = int(input("Enter your choice of  element "))
    list.append(num)
print(list)
sum_of_even = 0
sum_of_odd = 0
for i in list:
    if i % 2 == 0:
        sum_of_even += i
    else:
        sum_of_odd += i

print("Sum of even numbers in the given  list:", sum_of_even)
print("Sum of odd numbers in the given list:", sum_of_odd)