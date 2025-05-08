#11.What is a json file? Write a script to load and print a json file. (hint : use json library)
import json
  
  
# JSON string
a = '{"name": "Bob", "languages": "English"}'
  
# deserializes into dict 
# and returns dict.
y = json.loads(a)
  
print("JSON string = ", y)
print()
# JSON file
f = open ('data.json', "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()