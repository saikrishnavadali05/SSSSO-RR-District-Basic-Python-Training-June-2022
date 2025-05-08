# Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. Accept from the user the count of numbers and the actual numbers.
Number_Of_Digits_Going_to_Be_Added = int(input("Enter the number of Digits going to be added "))
Actual_Number = []
Odd_Number = []
Even_Number = []
for i in range(0,Number_Of_Digits_Going_to_Be_Added):
    value = int(input("Enter the Actual Number "))
    Actual_Number.append(value)
print("The Entered numbers are")    
print(Actual_Number)
for i in range(0,Number_Of_Digits_Going_to_Be_Added):
    if (Actual_Number[i]) % 2 == 0:
        Even_Number.append(Actual_Number[i])
    else:
        Odd_Number.append(Actual_Number[i])
print("The Even number out of", Actual_Number,"are", Even_Number)
print("The odd number out of", Actual_Number,"are", Odd_Number)


