# Python Program for cube sum of first n natural numbers
Total_Natural_Numbers = int(input("Total Number of Natural Numbers for which the sum of Cubes to be found "))
i = 0
Sum_of_Cube = 0
if Total_Natural_Numbers > 0:
    for Total_Natural_Numbers in range(1,Total_Natural_Numbers+1):
        Sum_of_Cube = Total_Natural_Numbers*Total_Natural_Numbers*Total_Natural_Numbers + Sum_of_Cube
        i = i - 1
print(Sum_of_Cube)

    