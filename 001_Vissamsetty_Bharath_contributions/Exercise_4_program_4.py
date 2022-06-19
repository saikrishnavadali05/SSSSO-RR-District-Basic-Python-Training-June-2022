"""

Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

Examples: 

Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

"""

#solution

# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final

if __name__ == "__main__":
# Driver Function
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum :", returnSum(dict))
