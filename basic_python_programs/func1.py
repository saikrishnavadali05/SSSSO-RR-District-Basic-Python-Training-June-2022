def square(a):
  '''Returns the square of a number'''
  return a * a

print(square.__doc__)

val = square(3)
print(val)
print(type(val))

val = square
print(val(2))

print("Number is %d" %5)
print("sum of %d and %d is 15" %(5, 10))
print("sum of %.2f %.2f and %.2f is 20" %(5.5, 10, 4.5))
