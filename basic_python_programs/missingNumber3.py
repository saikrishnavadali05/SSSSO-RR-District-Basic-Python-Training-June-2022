'''
Given an array containing n distinct numbers taken from m, m+1,..., n, 
find the one that is missing from the array.
'''

class test:
  def missingNumber(self, nums):
    num_set = set(nums)
    print(num_set)
    n = len(nums) + 1
    for number in range(min(num_set), max(num_set)):
      if number not in num_set:
        return number

obj = test()
lst = [2, 4, 5, 6, 7, 9, 3]
print(obj.missingNumber(lst))