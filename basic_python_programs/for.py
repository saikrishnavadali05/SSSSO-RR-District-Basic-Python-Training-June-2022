data = ['genesis', 'insoft', 'limited']
for x in data:
  print(x, len(x))

datacp = []

for x in data:   
  if len(x) > 6: datacp.insert(0, x)

print(datacp)

months = ['jan', 'feb', 'march', 'april']
for i in range(len(months)):
  print("month {}: {}".format(i + 1, months[i]))

months = ['july', 'august', 'september', 'october']
for num, name in enumerate(months, start = 7):
  print("month {}: {}".format(num, name))
