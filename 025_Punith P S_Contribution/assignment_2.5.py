# Given a list of numbers write a program to calculate the sum of odd and even numbers and 
# print the same. Accept from the user the count of numbers and the actual numbers.

number_lst = []

size = int(input("Enter the size for the list: "))
for i in range(size):
    val = int(input("enter the numbers for the list :"))
    number_lst.append(val)
print("\n",number_lst)

even_num_sum = 0
odd_num_sum = 0
for i in range(size):
    if number_lst[i] % 2 == 0:
        even_num_sum += number_lst[i]
    else :
         odd_num_sum +=  number_lst[i]
print("\nSum of even Numbers is", even_num_sum)
print("\nSum of odd Numbers is", odd_num_sum)

