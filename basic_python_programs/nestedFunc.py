lst = []
num = 10

def outer(n):
  lst.append(n) 
  print(lst)

  global num
  num = 20
  print(num)

  def func():
    num = 30
    print(num)
  return func
  
func = outer(2)
func()
func = outer(3)
func()

print(num)  