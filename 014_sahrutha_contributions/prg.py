#distribution of candies

total_candies = 10
no_of_candies = int(input())
if no_of_candies in range(1, 6):
	print('No. of Candies Sold:',no_of_candies)
	print('No. of Candies Left:',total_candies-no_of_candies)
else:
	print("Invalid Input")
	print('No. of Candies Left:',total_candies