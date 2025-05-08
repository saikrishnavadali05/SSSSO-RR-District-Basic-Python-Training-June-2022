"""
Given a dictionary with values list, extract key whose value has most unique values.

Input : test_dict = {“Gfg” : [5, 7, 9, 4, 0], “is” : [6, 7, 4, 3, 3], “Best” : [9, 9, 6, 5, 5]}
Output : “Gfg”

"""

#solution

# Python3 code to demonstrate working of
# Key with maximum unique values
# Using loop

# initializing dictionary
test_dict = {"Gfg" : [5, 7, 5, 4, 5],
			"is" : [6, 7, 4, 3, 3],
			"Best" : [9, 9, 6, 5, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

max_val = 0
max_key = None
for sub in test_dict:
	
	# test for length using len()
	# converted to set for duplicates removal
	if len(set(test_dict[sub])) > max_val:
		max_val = len(set(test_dict[sub]))
		max_key = sub

# printing result
print("Key with maximum unique values : " + str(max_key))
