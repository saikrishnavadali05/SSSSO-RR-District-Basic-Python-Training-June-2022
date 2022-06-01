
def outer(n):
  local1 = 20
  print(local1)

  def inner1():
    local1 = 30
    print(local1)

  def inner2():
    local1 = 40
    print(local1)

  def inner3():
    local1 = 50
    print(local1)

  return (inner1, inner2, inner3)

f = outer(2)
f1 = f[2]
f1()