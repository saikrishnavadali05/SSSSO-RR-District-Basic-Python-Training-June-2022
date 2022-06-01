# Execute on Python 2.7 compiler to see the difference in output

months = {4:'April', 2:'Feb', 5:'May'}
months[1] = 'Jan'
print(months)

print (months[2])
months[3] = 'March'

print(months)
print(months.keys())
print(months.values())

del months[2]

for key in months:
  print(key, months[key])

print(months.pop(3))
print(months)

print(5 in months)
print(3 in months)
print(months.get(1))
#del months 
months.clear()
print(months)