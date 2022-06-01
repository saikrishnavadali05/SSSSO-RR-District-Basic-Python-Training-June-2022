# Functions continued
def sumodd(n = 5):
  val = 0
  index = 1
  while (index <= n):
    # if even we continue with next iteration
    if (index % 2 == 0):
      index += 1
      continue

    # if odd we add it
    val += index
    index += 1
  return val

def funNotImplemented(): pass 

print("sumodd is", sumodd(3))
print("sumodd is", sumodd())

funNotImplemented()
