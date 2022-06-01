def funcVarDictionary(first, *arguments, **keywords):
  print("value of first argument:", first)
  for arg in arguments:
    print(arg)

  keys = keywords.keys()
  for kw in keys:
    print (kw, ':', keywords[kw])

funcVarDictionary(10, "How", k1 = 'v1')
funcVarDictionary("Hello", "How", "are", "you", k1='v1', k2='v2', k3='v3')

months_days = {'Jan': 31, 'Feb': 28, 'March': 31, 'April':30}
funcVarDictionary("months", **months_days)

