Dict = {} 
 
# Creating a Dictionary  with Mixed keys 
Dict = {'Name': 'Genesis', 1: [1, 2]} 
Dict[1] = 5, 6
Dict[2] = 2, 3, 4
print("\nDictionary with the use of Mixed Keys: ") 
Dict[3] = {'Nested' :{1 : 'Hyderabad', 2 : 'Telangana'}} 
print(Dict) 

print(Dict[3]['Nested'][2])
  
# Creating a Dictionary with dict() method 
Dict = dict({1: 'Genesis', 2: 'Insoft', 3:'Limited'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'Genesis'), (2, 'Hyderabad')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

cubes = {1: 1, 2:8, 3: 27, 4: 64, 5: 125}
for i in cubes:
  print(cubes[i])

print("Len = ", len(cubes))
