'''
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
'''

def singleNumber1(nums):
  unique = nums[0]
  for i in range(1, len(nums)):
    unique ^= nums[i]
  return unique

def singleNumber2(nums):
  no_duplicate_list = []
  for i in nums:
    if i not in no_duplicate_list:
      no_duplicate_list.append(i)
    else:
      no_duplicate_list.remove(i)
  return no_duplicate_list.pop()


def singleNumber3(nums):
  hash_table = {}
  for i in nums:
    try:
      hash_table.pop(i)
    except:
      hash_table[i] = 1
  return hash_table.popitem()[0]

lst = [1, 5, 2, 3, 2, 3, 1, 4, 4, 1, 1, 5, 5]
print(singleNumber1(lst))