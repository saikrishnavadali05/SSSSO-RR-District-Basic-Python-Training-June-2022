#What is a json file? Write a script to load and print a json file. (hint : use json library)
'''
The full form of JSON is Javascript Object Notation.
It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data.
Python supports JSON through a built-in package called JSON.
To use this feature, we import the JSON package in Python script. 
The text in JSON is done through quoted-string which contains the value in key-value mapping within { }. 
It is similar to the dictionary in Python.
'''
import json 
student={"name":"Divya",
          "Id":1,
          "Age":20,
          "Class":12,
          'Course':"MPC"}

with open("This is json file","w")as outfile:
    json.dump(student,outfile)

#output
#The data is stored in (This is json file).