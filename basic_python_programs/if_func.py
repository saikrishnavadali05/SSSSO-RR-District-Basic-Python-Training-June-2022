import inspect

def line_number():
   '''Returns the current line number in our program'''
   return inspect.currentframe().f_back.f_lineno

x = int(input("Please enter an integer: "))
if x < 0:
  print(line_number(), 'Less than zero')
elif x == 0:
  print(line_number(), 'Zero')
else:
  print(line_number(), 'greater than zero')