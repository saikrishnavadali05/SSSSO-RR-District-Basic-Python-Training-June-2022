# Write a program to create variables storing values for each datatype. print the object identities of all the created variables.Next,
# convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.

Enter_String = input("Enter a String ")
print("The Entered String is",Enter_String)

Set_String = set(Enter_String)
print("The String is converted to set as",Set_String)

Tuple_String = tuple(Enter_String)
print("The String is converted to tuple as",Tuple_String)

Frozenset_String = frozenset(Enter_String)
print("The Number is converted to frozenset as",Frozenset_String)

# Dict_String = dict(Enter_String)

Enter_Number = int(input("Please Enter Number "))
print("The Entered number is", Enter_Number)

Float_Number = float(Enter_Number)
print("The Number is converted to float as", Float_Number)

Flag = False
Enter_Comparizon_number1 = int(input("Enter the number1 to compare "))
Enter_Comparizon_number2 = int(input("Enter the number2 to compare "))
if (Enter_Comparizon_number1 == Enter_Comparizon_number2):
    Flag = True
    print("The Flag is",Flag, "which means both the numbers are equal")
elif (Enter_Comparizon_number1 > Enter_Comparizon_number2):
    Flag = True
    print("The Flag is",Flag, "which means",Enter_Comparizon_number1, "is greater than", Enter_Comparizon_number2)
else:
    Flag = True
    print("The Flag is",Flag, "which means",Enter_Comparizon_number2, "is greater than", )