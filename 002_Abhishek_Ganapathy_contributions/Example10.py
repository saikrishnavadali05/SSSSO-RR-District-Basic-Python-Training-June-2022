# Write a function that take string as a parameter. the string is given by the user as input. the final output from the function is to reverse the string.

def Reversed(GiveString):
     return GiveString[::-1]
Enter_String = input("Give a string ")
Global_Reverse_String = Reversed(Enter_String)
print("The Reversed String of",Enter_String,"is",Global_Reverse_String)

# Write a function that take three integers and compare which the largest and smallest among the them. take input from the end user.

def CompareMax(List):
    return max(List)

def CompareMin(List):
    return min(List)

Number_List = list(input("Enter 3 numbers "))
ComparisonMax = CompareMax(Number_List)
ComparisonMin = CompareMin(Number_List)

print("The Maximum Number is",ComparisonMax)
print("The Minimum number is", ComparisonMin)
