import collections

d = collections.OrderedDict(
  [('a', 'A'), ('b', 'B'), ('c', 'C')]
)

print('Before:')
for k, v in d.items():
  print(k, v)

d.move_to_end('b')

print('\nmove_to_end():')
for k, v in d.items():
  print(k, v)

d.move_to_end('b', last=False)

print('\nmove_to_end(last=False):')
for k, v in d.items():
  print(k, v)
