
#method1
list1=[int(item) for item in input("Enter the list items:").split()]
print("maximum Element",max(list1))
print("minimum element",min(list1))
#method2
list = []
num = int(input("How many elements in list: "))

for i in range(num):
  numbers = int(input('Enter number '))
  list.append(numbers)
 
print("\nMaximum element in the list is :", max(list))
print("Minimum element in the list is :", min(list))

