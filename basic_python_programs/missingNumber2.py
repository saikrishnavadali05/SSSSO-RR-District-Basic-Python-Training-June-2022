'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

sum = (n * (n+1))/2
'''

def missingNumber(self, nums):
  expected_sum = len(nums)*(len(nums)+1)//2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

lst = [0, 2, 4, 8, 6, 7, 9, 3, 1]
print(missingNumber(lst))