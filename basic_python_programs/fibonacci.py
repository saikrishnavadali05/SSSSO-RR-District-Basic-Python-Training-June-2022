# Fibonacci series: the sum of two elements defines the next
def fib1():
  n1, n2 = 0, 1
  while n2 < 15:
    print(n2)
    n1, n2 = n2, n1 + n2

# Return a list containing the Fibonacci series up to n
def fib2(n): 
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b) 
    a, b = b, a + b
  return result

print (__name__)

if __name__ == "__main__":
  fib1()
  print("After call to fib1()")
  print(fib2(20))
