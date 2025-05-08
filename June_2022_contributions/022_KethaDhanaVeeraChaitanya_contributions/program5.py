Dict_student = {
  "name": "chaitanya",
  "roll_number": "CSEAL&LML",
  "year": 1,
  "age" : 19
}
#for printing both key value pairs 

print(Dict_student)
for key,value in Dict_student.items():
  print(key, ':',value)
  
  #printing only values

print(Dict_student.values())