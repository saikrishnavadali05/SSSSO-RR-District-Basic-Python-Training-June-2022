"""
11.What is a json file? 
Write a script to load and print a json file. (hint : use json library)
"""

"""
JSON is a lightweight data-interchange the format and it will written 
a plain text in JavaScript Object Notation(JSON).
It is used send data between the computers
"""

import json

dictionary = {
    'name':'Ranjith',
    'rollno':3,
    'cgpa':7.1,
    'phone': 8179176017
}

json_obj = json.dumps(dictionary)

f = open('sample.json','w')

f.write(json_obj)
