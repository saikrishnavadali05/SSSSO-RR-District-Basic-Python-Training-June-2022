details = {"name": "steve","education":"Reed College","born":1995}
for key,value in details.items():
  print(key,value)
details["died"]="2011"  
print(details)
del details["education"]
for key in details:
    print(key,details[key])
#To print duplicate dictionary
details_duplicate = details.copy()    
details.clear()
print(details)
print("the entire duplicate dictionary is :")
print(details_duplicate)
