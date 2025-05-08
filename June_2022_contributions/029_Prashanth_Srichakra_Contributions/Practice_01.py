# Write a program to find the second largest element in a list

list = []
list_size = int(input("Enter size of list: "))
for i in range(0,list_size):
    elem = int(input(f"Enter element {i}: "))
    list.append(elem)

list.sort()

print("Second Largest element in given list is", list[list_size-2])