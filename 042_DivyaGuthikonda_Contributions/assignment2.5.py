# Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same.
# Accept from the user the count of numbers and the actual numbers.

lst = []
EvenSum = 0
OddSum = 0

n = int(input("Enter the number of elements in a list: "))
for i in range(1, n + 1):
    ele = int(input())
    lst.append(ele)
print(lst)
for j in range(n):
    if(lst[j] % 2 == 0):
        EvenSum = EvenSum + lst[j]
    else:
        OddSum = OddSum + lst[j]

print("Sum of odd numbers", EvenSum)
print("Sum of even numbers:", OddSum)

#output
#Enter the number of elements in a list: 5
#34
#56
#77
#45
#2
#[34, 56, 77, 45, 2]
#Sum of odd numbers 92
#Sum of even numbers: 122
