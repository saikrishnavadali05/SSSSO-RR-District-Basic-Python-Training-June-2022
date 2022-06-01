# dictionary arguments
def funcdictionary(**keywords):
  keys = keywords.keys()
  for kw in keys:
    print (kw, ':', keywords[kw])

funcdictionary(k1 = 'v1')
funcdictionary(k1='v1', k2='v2', k3='v3')

months_days = {'Jan': 31, 'Feb': 28, 'March': 31, 'April':30}
funcdictionary(**months_days)