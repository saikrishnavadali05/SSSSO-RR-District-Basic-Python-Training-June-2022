months_days = {'Jan': 31, 'Feb': 28, 'March': 31}
months_days['April'] = 30
print(months_days.keys())
print(months_days.items())
print(months_days.values())

keys = list(months_days.keys())
print(keys)
keys.sort()
for key in keys:
  print(key, months_days[key])
