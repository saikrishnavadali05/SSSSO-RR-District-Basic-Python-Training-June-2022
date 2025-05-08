# Python Program for factorial of a number
Number = int(input("Enter the number for which you want to know the Factorial "))
i = 1
Solution = 1
if Number > 1:
    for i in range(1,Number + 1):
        Solution = Number*Solution
        Number = Number-1
print(Solution)
