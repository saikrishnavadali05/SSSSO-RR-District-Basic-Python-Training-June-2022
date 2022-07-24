def sum_List(List,Length):
    sum = 0
    for i in range(0,Length):
        sum = int(List[i]) + sum
        i = i + 1
    return sum
    
Number_List = list(input("Enter the number "))
Length_of_List = len(Number_List)
sum_of_the_list = sum_List(Number_List,Length_of_List)
print("The sum of the numbers in the list",Number_List,"with length",Length_of_List,"is",sum_of_the_list)
