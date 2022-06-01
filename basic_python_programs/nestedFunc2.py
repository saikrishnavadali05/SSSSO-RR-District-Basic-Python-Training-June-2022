def outer(n):
  local1 = 20
  print(local1)

  def inner():
    local1 = 30
    print(local1)

    def innermost():
      local1 = 40
      print(local1)
    return innermost
  return inner

inner = outer(2)
innermost = inner()
innermost()