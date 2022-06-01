'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.
'''

def missingNumber(nums):
  missing = len(nums)
  for i, num in enumerate(nums):
    missing ^= i ^ num

  return missing

lst = [0, 2, 4, 8, 6, 7, 9, 3, 1]
print(missingNumber(lst))