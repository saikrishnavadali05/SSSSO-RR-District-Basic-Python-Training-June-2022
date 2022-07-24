Give_String = str(input("Enter String "))
Count = 0
Numericals = list()
print("The Lower case of the string",Give_String,"is",Give_String.lower())
print("The Lower case of the string",Give_String,"is",Give_String.upper())
Give_String_List = list(Give_String)
print(Give_String_List)
for i in range(0,len(Give_String_List)):
    if(Give_String_List[i].isdigit()):
        Number = Give_String_List[i]
        Numericals.append(Number)
        Count =  Count+1
print("Number of digits in the string is",Count)
print("Numricals in the string is",Numericals)
print("The length of the string is ",len(Give_String))