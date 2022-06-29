list=[]
n=int(input("enter the number of elements :"))
for i in range(0,n):
    element = int(input())
    list.append(element)
print(list)
print("the maximum element in the list is",max(list))
print("the minimum element in the list is ",min(list))
print()

#Finding maximum and minimum in the given list without using inbuilt functions

maximum=list[0]
for i in range(0,n):
    if list[i] > maximum:
        maximum=list[i]
print("the maximum value of the list is ",maximum)        
minimum = list[0]
for i in range(0,n):
    if list[i] < minimum:
        minimum = list[i]
print("The minimum element in the list is ",minimum)        

