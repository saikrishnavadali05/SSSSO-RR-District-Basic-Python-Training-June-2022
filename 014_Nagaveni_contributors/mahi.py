#1.python function:
'''print("my name is mahi","iam studing IT")
print("my name is mahi","iam studing IT",sep='@',end='\n')
# Header for python script:
# runing output in python script,
#    Indentation:

print("computer")          #this is indentation:
print("python programing")  #this is indentation:
#    continuation lines
print("my name is hema","iam studing diplama","she is very sencitive") #continuation lines
print("my name is hema","iam studing diplama","she is very sencitive",sep="\t",end=" ")
#3.DATA TYPES:

int=20
float=2.5
complex=2+3j
print("enter the variables values is:",int,float)
int=input("enter the  value is:")
print(int)
float=input("enter the  value is:")
print(float)
complex=input("enter the value i:")
print("ENTER THE VARIABLE VALUES IS:",int,"\t",float,"\t",complex,)
#boolen values:
age1=25
age2=20
if age1>age2: #it is true:  this is boolen value
    print("age1 is oldest") 
#else:         #it is false: this is boolen value
    print("age2 is oldest")
if age1<age2: #it is true:  this is boolen value
    print("age1 is oldest") 
elif age1>age2:
    print("age2 is oldest")
else:
    print("age1 is not oldest")
#frozenset:

person={"name":"gowtham","age":"25","gender":"male"}
f_set=frozenset(person)
print("enter the forzenset:",f_set)
print()
words={"python","life","programing"}
f_set=frozenset(words)
print(type(words))
print(type(f_set))
print("enter the forzenset:",f_set)
#conversion one data to another data :
a=35
b=30.5
c=2+5j
m=float(a)
n=complex(b)
o=int(b)
print("enter the values:",m,"\t",n,"\t",o) 
#data types:    exercise-1
#Q.Tell the given type of variable ?
name="mahendhra"
#a=type(name)
print(type(name))
#Q.Which method is used to find the type of the variable for a=20 ?
a=20
print(type(a)) 
#Q.Tell the correct answer from thefllows?
a="10"
b="ram21"
c=12
#1_d=6
print("enter the correct answer is:",a,b,c)
#Q.Assign the values to the variable and print it?
name_of_student=60
print(name_of_student)
#Q.Write a word in the for the variable and print it
nameWord="MahiNaga"
print(nameWord)
#Q.Write the scientific notation for given float number 0.002569 is ?
#float_number=o.oo2569

#  4. VARIABLES:
# python variable
x=13
_x=14
y=type(_x)
print(y)
print("enter the variables:",x,_x)
#create good names:
nameStudent="mahi" 
a=nameStudent
studentAge="25"   
b=studentAge
studentWeight="75" 
c=studentWeight
print("enter the values:",a,b,c)
print('enter the values:',"\"",a,"\"","\t",b,"\t",c)
print("ENTER THE VALUES:","\"",a,"\"","\n","\r",b,"\a","\n","\a",c)
# 5.USER INPUT
name=input("enter the name:")
age=input('enter the age:')
print(type(name))
print()               '''

 
#parameter,input string,reverse string
def variable(string) :
    string="python"
    for i in string:
        string=i+string
    return string
string=str(input("enter the string "))
result=variable(string)
print(result) 
print(string)













