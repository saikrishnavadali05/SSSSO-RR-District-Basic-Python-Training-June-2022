#  Given a Full name stored in a input file input_name.txt which contains first name, middle name and last name.
#  All the first, middle and last name are seperated by spaces.
#  Print the output in the following order: Last Name, First Name, middle name.
#  Next, Save the last name in last_name.txt file. Save the first name in first_name.txt.
#  Save the middle name in middle_name.txt file.
file=open('input_name.txt','r')
data=file.read()#input is taken from input_name.txt
file.close()
h=open('input_name.txt','r')
content=h.readlines()
print(data)
d=data.split()
print(d)#splitting the data
def lastname(d):
    a=d[2]
    return a
def firstname(d):
    b=d[0]
    return b
def middlename(d):
    c=d[1]
    return c

f=open("last_name.txt","a")
print("Last name :",lastname(d),file=f)
f.close()

f=open("first_name.txt","a")
print("first name :",firstname(d),file=f)
f.close()

f=open("middle_name.txt","a")
print("middle name :",middlename(d),file=f)
f.close()

#output stored as specified in question
#Divya Rao Guthikonda
#['Divya', 'Rao', 'Guthikonda']

