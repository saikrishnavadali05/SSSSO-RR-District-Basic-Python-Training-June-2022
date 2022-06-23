# Python code to remove duplicate elements
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
res = tuple(map(lambda i, j: i + j, test_tup1, test_tup2))
print("Resultant tuple after addition : " + str(res))