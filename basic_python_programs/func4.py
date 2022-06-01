# variable arguments 
def funcvarArgs(first, *arguments):
  print("value of first argument:", first)
  for arg in arguments:
    print(arg)

funcvarArgs(10)
funcvarArgs(20, "How")
funcvarArgs("Hello", "How", "are", "you")
