Number_list = list(input("Get list of numbers "))
Odd_List = list()
Even_List = list()
Sum_of_Even = 0
Sum_of_Odd = 0
for i in range(0,len(Number_list)):
    if(int(Number_list[i]) % 2) == 0:
        Result = Number_list[i]
        Even_List.append(Result)
    else:
        Result1 = Number_list[i]
        Odd_List.append(Result1)
print("The Odd number list ",Odd_List)
print("The even number list ",Even_List)
for i in range(0,len(Even_List)):
    Sum_of_Even = int(Even_List[i]) + Sum_of_Even

for i in range(0,len(Odd_List)):
    Sum_of_Odd = int(Odd_List[i]) + Sum_of_Odd

print("The Sum of Even numbers",Even_List, "is", Sum_of_Even)
print("The Sum of Odd numbers",Odd_List, "is", Sum_of_Odd)


    
