lst = []
n = int(input("Enter number of elements in list"))
for i in range(n):
    ele = int(input("Enter element"))
    lst.append(ele)
print(lst)
sum_of_even = 0
sum_of_odd = 0
for i in lst:
    if i % 2 == 0:
        sum_of_even += i
    else:
        sum_of_odd += i

print("Sum of even numbers in list:", sum_of_even)
print("Sum of odd numbers in list:", sum_of_odd)