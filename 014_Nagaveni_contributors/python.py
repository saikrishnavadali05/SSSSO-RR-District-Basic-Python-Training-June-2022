#DATA TYPES THERE ARE TREE TYPES:1.numeric,2.mapping,3.sequances
#1.Numeric: integer  , float , comflex ;
a=20
b=35.5
c=2+3j
print("enter the variables is :",a,"\n",b,"\n",c)    #20   , #35.5   , #(2+3j) 

#creat a convarsion of numeric variables:
m=float(a)
n=int(b)
o=complex(b)
print("enter the values:",m,"\t",n,"\t",o)        #20.0   35      (35.5+0j)  
#2.MAPPING:1.dictionary,2.boolen:
#1.DICTIONARY:keys,values,items,pop,update,clear:
var={"name":'mahi',"age":26,"ph.no":[839235367]}
print(var.keys())                                    #dict_keys(['name', 'age', 'ph.no'])
var={"name":'mahi',"age":26,"ph.no":[839235367]}
print(var.values())                                  #dict_values(['mahi', 26, [839235367]])
var={"name":'mahi',"age":26,"ph.no":[839235367],"aadhar.no":[645034274623],"address":"palamaner"}
print(var.items()) #dict_items([('name', 'mahi'), ('age', 26), ('ph.no', [839235367]), ('aadhar.no', [645034274623]), ('address', 'palamaner')])
var.pop("aadhar.no","ph.no")
print(var)             #{'name': 'mahi', 'age': 26, 'ph.no': [839235367], 'address': 'palamaner'}
var.update({"gender":"male"})
print(var)             #{'name': 'mahi', 'age': 26, 'ph.no': [839235367], 'address': 'palamaner', 'gender': 'male'}
var.clear()
print(var)             #{}     

dic={"name":'guna',"age":14}
print(dic)
dic.update({"gender":'female',"address":'palamaner'})
print(dic)              #{'name': 'guna', 'age': 14, 'gender': 'female', 'address': 'palamaner'}
dic.pop("name")
print(dic)              #{'age': 14, 'gender': 'female', 'address': 'palamaner'}
print(dic.keys(),"\t",dic.values())  #dict_keys(['age', 'gender', 'address'])          dict_values([14, 'female', 'palamaner'])
print(dic.items())                   #dict_items([('age', 14), ('gender', 'female'), ('address', 'palamaner')])
print(dic.clear())       #None       
#Built in methods and functions:max,min,len,sorted;
dic={"names","age","address","phoneNumber"}
maximum=max(dic)
minimum=min(dic)
sort=sorted(dic)
lenth=len(dic)
print(maximum,"\n",minimum,"\n",sort,"\n",lenth)  #phoneNumber , # address , #['address', 'age', 'names', 'phoneNumber'] ,# 4
                                                   
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

#3.Create a sequences:List,tuple,string;
#list OPERATORS:
a=['github','python','java']
b=['program','course','language']
print("enter the words:",a,"\n",'\t','\t',b)   #['github', 'python','java']   #['program', 'course', 'language']
print("enter the words:",a+b)            #['github', 'python', 'java', 'program', 'course', 'language']
c=[1,8,9]+[9,10,12]
print("enter the add values:",c)       #[1, 8, 9, 9, 10, 12]
d=["a","num","20"]
d+=a
print("enter the var is:",d)        # ['a', 'num', '20', 'github', 'python', 'java']  
#repetetive(*) operator:
a=[1000,500,600]
print("enter the repetetive values:",a*4)
b=[9,8,7]==[9,8,7]
c=[3,4,5]==[3,6,5]
print("b is :",  b,"\n","c is :",c)   #b is : True  , #c is : False
b=[9,8,7]!=[9,8,7]                    
c=[3,4,5]!=[3,6,5]
print("b is :",  b,"\n","c is :",c)    #b is : False  ,   #c is : True
b=[9,8,7]is[9,8,7]                    
c=[3,4,5]is[3,6,5]
d=[1,2,3]is[3,2,1]
print("b is :",b,"\n","c is :",c,"\n","d is:",d)   #b is : False  ,#c is : False  , #d is: False  
b=[9,8,7]is not[9,8,7]                    
c=[3,4,5]is not[3,6,5]
d=[1,2,3]is not[3,2,1]
print("b is :",b,"\n","c is :",c,"\n","d is:",d)   #b is : True   ,#c is : True    ,#d is: True  
names=["harish","mahi","ganesh"]+["guna","siva","madhu"]
print("names is:",names)         #['harish', 'mahi', 'ganesh', 'guna', 'siva', 'madhu']
print("mahi" in names )        #True
print("guna" in names )      #True   
print("python" in names )  #False             
#create a BUILTING FUNCTION AND METHODS:mxa,min,len,sorted,sum ,"reversed"
a=[1,4,5,8,7,3]
maximum=max(a) 
print("enter the maximum value is:",maximum)  #enter the maximum value is: 8
minimum=min(a)
print("enter the minimum value is:",minimum) # 1
lenth=len(a)
print("enter the lenth value is:",lenth)    #  6
sort=sorted(a)
print("enter the sort values:",sort)       # [1, 3, 4, 5, 7, 8]
print("enter the sort is:",c)
add=sum(a)
print("enter the add is:",add)            #28     














