import sys

# __debug__ is true by default, unless we run 
# using -O (optimized code)
# python -O assert.py

print(__debug__)

# assert comes into affect only when __debug__ is true

num = int(input('Enter a positive number: '))
print(num)
assert(num > 0), 'Only positive numbers are allowed!'

def chkassert(num):
  assert(type(num) == int)

chkassert('india')

sys.exit()
