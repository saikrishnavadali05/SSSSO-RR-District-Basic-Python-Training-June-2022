print("5.	Write a program to print all the details of a student by \
storing all of his details in a dictionary by retrieveing the values \
from keys. Next, Print the entire dictionary. Next, print each and \
every key value pair seperately. Next, print only values (Don't print keys).")

my_dict={"name":"Taraka vani","age":8,"class":2,"roll no":10}
print("my student details are:",my_dict)
print("value of key1: ",my_dict.get("name"))
print("value of key2: ",my_dict.get("age"))
print("value of key3: ",my_dict.get("class"))
print("value of key4: ",my_dict.get("roll no"))
for s in my_dict:
    print("my student details is:",s)
