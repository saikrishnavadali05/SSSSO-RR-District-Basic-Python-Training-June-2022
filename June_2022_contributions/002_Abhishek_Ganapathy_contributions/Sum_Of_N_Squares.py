Total_Natural_Numbers = int(input("Total Number of Natural Numbers for which the sum of Squares to be found "))
i = 0
Sum_of_Square = 0
if Total_Natural_Numbers > 0:
    for Total_Natural_Numbers in range(1,Total_Natural_Numbers+1):
        Sum_of_Square = Total_Natural_Numbers*Total_Natural_Numbers + Sum_of_Square
        i = i - 1
print(Sum_of_Square)