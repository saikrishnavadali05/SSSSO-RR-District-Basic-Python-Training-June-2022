#Given a list of numbers write a program
#  to calculate the sum of odd and even numbers
#  and print the same.
#  Accept from the user the count of 
# numbers and the actual numbers.

List = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List.append(value)

for j in range(Number):
    if(List[j] % 2 == 0):
        Even_Sum = Even_Sum + List[j]
    else:
        Odd_Sum = Odd_Sum + List[j]

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)