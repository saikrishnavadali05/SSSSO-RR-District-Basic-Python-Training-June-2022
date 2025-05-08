#string operations

str1 = "good morning"
str2 = "welcom_all"
print(" the id values of str1 and str2 are :",id(str1), id(str2))

 # string obects do not supprt item assignment , as immutable datatype

to_add = "hello_all"
#to_add[2] = 'i'
#print(to_add) 

#appending a new character in a exixting string

str1 = str1[:2] + 'i' +  str1[9:]
print("modified :",str1 ,   "the modified id value ",id(str1))

#finding the index of  each character in a string using index()

student_name = "ram_prasad"
print("the index of a letter in  :"  , student_name.index('a'))
print(student_name.index('sad'))        #index of substring can be obtained
print('e' in student_name)              # False : because the letter 'e' doesnt exist in the string
print(student_name.replace('a' , 'e'))
print(student_name.upper() , student_name.lower())
print(student_name.capitalize())        # to capitalise the  first character
sym = '='
print(sym.join(('chand','jaanu','dad', 'mom')))
Name = "india"
print("Printing name 3times: ", Name*3, "\n" "Length of name is: ",len(Name))
print(Name[0:5])
Str_name = "iamfine"
print("Is Str_name contains numbers: ", Str_name.isalnum(), "\n" "Is string name contains Alphabets: ", Str_name.isalpha())
val = "673"
print(val.isdigit())
Name = "Multiple_Wishes"
print(Name.isalpha())
 
#eval() to evaluate the passed string
a = 5.2 + 8
print(eval('a')) 
