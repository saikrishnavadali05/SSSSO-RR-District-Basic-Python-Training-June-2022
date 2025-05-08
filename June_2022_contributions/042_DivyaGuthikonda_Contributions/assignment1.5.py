#Write a program to print all the details of a student by storing all of his details in a dictionary \n
# by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every \n
# key value pair seperately. Next, print only values (Don't print keys).
details = {
             "Name": "Steve",
             "Roll No.": 10,
             "Education": "MCS",
             "Institution": "Reddy College",
             "Born": 1955
           }
print("The dictionary is : ",details)
print()
print("Print only values")
for k,v in details.items():
    print(v)
print()
print("Print the key value pair: ")
for k,v in details.items():
    print(k,":",v)
#(Output)
'''
The dictionary is :  {'Name': 'Steve', 'Roll No.': 10, 'Education': 'MCS', 'Institution': 'Reddy College', 'Born': 1955}

Print only values
Steve
10
MCS
Reddy College
1955

Print the key value pair:
Name : Steve
Roll No. : 10
Education : MCS
Institution : Reddy College
Born : 1955
'''