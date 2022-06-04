"""
Sum of tuple elements

The original tuple is : (7, 8, 9, 1, 10, 7)
The summation of tuple elements are : 42

"""







#solution

# Python3 code to demonstrate working of
# Tuple summation
# Using list() + sum()

# initializing tup
test_tup = (7, 8, 9, 1, 10, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using list() + sum()
res = sum(list(test_tup))

# printing result
print("The summation of tuple elements are : " + str(res))
