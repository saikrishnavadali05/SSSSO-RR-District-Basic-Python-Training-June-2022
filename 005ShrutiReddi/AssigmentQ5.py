#Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. 
# Accept from the user the count of numbers and the actual numbers.

# Using For Loop with Range

Even_Sum = 0
Odd_Sum = 0

num_list = [36, 45, 78, 89, 12, 61]

# Print the Original List
print("Original List: ", num_list)

for x in range(len(num_list)): # for x in the list and total count of the list
    if(num_list[x] % 2 == 0): 
        Even_Sum = Even_Sum + num_list[x]# will add all even numbers if condiitions or else add odd as per below condition
    else:
        Odd_Sum = Odd_Sum + num_list[x]

print("\nThe Sum of Even Numbers in the Given List =  ", Even_Sum)
print("The Sum of Odd Numbers in the Given List  =  ", Odd_Sum)
