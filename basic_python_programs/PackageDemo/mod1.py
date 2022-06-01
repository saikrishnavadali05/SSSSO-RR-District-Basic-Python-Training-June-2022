import PackageDemo.mod2

def f():
  global x
  x = 6

def getX():
  return x

def main():
  x = 5
  f()
  print(x)
  PackageDemo.mod2.g()
  x += 2
  print(x)
