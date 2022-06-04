"""
Maximum and Minimum in a Set

Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
Output : max is 65

"""

#solution

# Python code to get the maximum element from a set
def MAX(sets):
	return (max(sets))
	
# Driver Code
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(MAX(sets))

# Python code to get the minimum element from a set
def MIN(sets):
	return (min(sets))
	
# Driver Code
sets = set([4, 12, 10, 9, 4, 13])
print(MIN(sets))

